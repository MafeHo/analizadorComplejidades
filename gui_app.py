import customtkinter as ctk
from tkinter import filedialog, messagebox
import threading
import sys
import os
from io import StringIO
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import re

# --- CORRECCIÓN DE IMPORTACIÓN ---
# Como este archivo está en la raíz, importamos 'analyze_algorithm' desde el paquete 'src'
# Asegúrate de que exista un archivo __init__.py en la carpeta src (aunque en Python 3 suele funcionar sin él)
try:
    from src.main import analyze_algorithm
except ImportError as e:
    print(f"Error de importación: {e}")
    print("Asegúrate de que la estructura sea:")
    print("  ANALIZADOR/")
    print("    gui_app.py")
    print("    src/")
    print("      main.py")
    sys.exit(1)

# Configuración inicial de diseño
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class OutputRedirector(object):
    """Clase auxiliar para redirigir los prints a la caja de texto de la GUI"""
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.configure(state="normal")
        self.text_widget.insert("end", string)
        self.text_widget.see("end")
        self.text_widget.configure(state="disabled")

    def flush(self):
        pass

class AlgorithmAnalyzerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Analizador de Complejidad Híbrido (ANTLR + LLM)")
        self.geometry("1100x700")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.current_file_path = None

        # --- PANEL IZQUIERDO ---
        self.sidebar_frame = ctk.CTkFrame(self, width=300, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Analizador\nAlgorítmico", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.btn_load = ctk.CTkButton(self.sidebar_frame, text="Cargar Archivo", command=self.load_file)
        self.btn_load.grid(row=1, column=0, padx=20, pady=10)

        self.code_label = ctk.CTkLabel(self.sidebar_frame, text="Editor de Código:", anchor="w")
        self.code_label.grid(row=2, column=0, padx=20, pady=(10, 0))

        self.code_input = ctk.CTkTextbox(self.sidebar_frame, width=280, height=250, font=("Consolas", 12))
        self.code_input.grid(row=3, column=0, padx=20, pady=(5, 20))
        
        default_code = """MergeSort(A, n)
begin
    If (n > 1) then
    begin
        mitad <- n / 2;
        CALL MergeSort(A, mitad);
        CALL MergeSort(A, mitad);
        for i <- 1 to n do
        begin
            temp <- A[i];
        end;
    end;
end;"""
        self.code_input.insert("0.0", default_code)

        self.translate_switch = ctk.CTkSwitch(self.sidebar_frame, text="Traducir Lenguaje Natural")
        self.translate_switch.grid(row=4, column=0, padx=20, pady=10)

        self.analyze_button = ctk.CTkButton(self.sidebar_frame, text="EJECUTAR ANÁLISIS", fg_color="green", hover_color="darkgreen", command=self.start_analysis_thread)
        self.analyze_button.grid(row=5, column=0, padx=20, pady=20)
        
        self.visualize_btn = ctk.CTkButton(self.sidebar_frame, text="Ver Pila de Recursión", fg_color="#E04F5F", hover_color="#C03545", command=self.open_stack_visualizer)
        self.visualize_btn.grid(row=6, column=0, padx=20, pady=10)

        # --- PANEL DERECHO ---
        self.right_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.right_frame.grid(row=0, column=1, sticky="nsew")
        self.right_frame.grid_rowconfigure(1, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)

        # 1. Panel de Gráfica
        self.plot_frame = ctk.CTkFrame(self.right_frame, height=250, fg_color=None)
        self.plot_frame.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        
        self.console_label = ctk.CTkLabel(self.right_frame, text="Resultados y Trazabilidad:", anchor="w")
        self.console_label.grid(row=1, column=0, padx=20, pady=(0,5), sticky="w")

        # 2. Consola
        self.console_output = ctk.CTkTextbox(self.right_frame, font=("Consolas", 11), state="disabled")
        self.console_output.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="nsew")

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            self.current_file_path = file_path
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.code_input.delete("0.0", "end")
                self.code_input.insert("0.0", content)
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo leer el archivo: {e}")

    def open_stack_visualizer(self):
        console_content = self.console_output.get("0.0", "end")
        if not console_content.strip():
            messagebox.showwarning("Aviso", "Primero ejecuta un análisis.")
            return
        StackVisualizerWindow(self, console_content)

    def start_analysis_thread(self):
        self.analyze_button.configure(state="disabled", text="Analizando...")
        threading.Thread(target=self.run_analysis).start()

    def run_analysis(self):
        self.console_output.configure(state="normal")
        self.console_output.delete("0.0", "end")
        self.console_output.configure(state="disabled")

        code_text = self.code_input.get("0.0", "end").strip()
        if not code_text:
            self.after(0, lambda: self.analyze_button.configure(state="normal", text="EJECUTAR ANÁLISIS"))
            return

        temp_filename = "temp_gui_input.txt"
        with open(temp_filename, "w", encoding="utf-8") as f:
            f.write(code_text)

        old_stdout = sys.stdout
        sys.stdout = OutputRedirector(self.console_output)

        complexity_result = "Desconocida" # Valor por defecto

        try:
            should_translate = bool(self.translate_switch.get())
            
            # Llamada a la función importada
            complexity_result = analyze_algorithm(temp_filename, translate_mode=should_translate)
            
            # Actualizamos la gráfica con el resultado real
            self.after(0, lambda: self.update_graph(complexity_result))

        except Exception as e:
            print(f"\nERROR CRÍTICO EN GUI: {e}")
        finally:
            sys.stdout = old_stdout
            self.after(0, lambda: self.analyze_button.configure(state="normal", text="EJECUTAR ANÁLISIS"))
    
    def update_graph(self, complexity_str):
        """
        Dibuja la gráfica basándose en la complejidad CALCULADA por el sistema.
        complexity_str: String como "O(n^2)", "Theta(n log n)", etc.
        """
        
        # Limpiar gráfica anterior
        for widget in self.plot_frame.winfo_children():
            widget.destroy()

        # Crear figura matplotlib
        fig, ax = plt.subplots(figsize=(5, 2.5), dpi=100)
        fig.patch.set_facecolor('#2b2b2b')
        ax.set_facecolor('#2b2b2b')
        
        x = np.linspace(1, 20, 100) # Rango de n
        
        # Normalizamos el string para facilitar la búsqueda
        comp_clean = str(complexity_str).lower().replace(" ", "")
        
        # Lógica para determinar la función Y basada en la complejidad REAL
        y = x # Default lineal
        title = f"Visualización: {complexity_str}"
        color = 'white'

        if "n^2" in comp_clean or "quadratic" in comp_clean:
            y = x**2
            color = '#FF5733' # Rojo naranja
        elif "nlog" in comp_clean or "n*log" in comp_clean:
            y = x * np.log2(x)
            color = '#33FF57' # Verde lima
        elif "logn" in comp_clean:
            y = np.log2(x)
            color = '#33C1FF' # Azul claro
        elif "2^n" in comp_clean:
            y = 2**x
            color = '#FF33A8' # Rosa fuerte
        elif "n^3" in comp_clean:
            y = x**3
            color = '#C70039' # Rojo oscuro
        elif "1" in comp_clean and "n" not in comp_clean: # O(1)
            y = np.ones_like(x)
            color = '#FFC300' # Amarillo
        else:
            # Si no reconoce (ej. O(n)), asume lineal por defecto
            y = x
            color = '#DAF7A6' 

        ax.plot(x, y, color=color, linewidth=2)
        ax.set_title(title, color='white', fontsize=10, fontweight='bold')
        ax.set_xlabel("Tamaño de entrada (n)", color='white', fontsize=8)
        ax.set_ylabel("Tiempo / Operaciones", color='white', fontsize=8)
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.grid(True, linestyle='--', alpha=0.2)

        # Insertar en Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side="top", fill="both", expand=True)


class StackVisualizerWindow(ctk.CTkToplevel):
    def __init__(self, parent, console_text):
        super().__init__(parent)
        self.title("Visualización de Pila de Llamadas (Stack Frames)")
        self.geometry("600x600")
        
        self.canvas = ctk.CTkCanvas(self, bg="#1e1e1e", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.console_text = console_text
        self.steps = self.parse_trace_table(console_text)
        
        if not self.steps:
            self.canvas.create_text(300, 300, text="No se detectó tabla de recursión en el análisis.", fill="white", font=("Arial", 14))
        else:
            self.animate_stack()

    def parse_trace_table(self, text):
        steps = []
        # Busca líneas que empiecen por "| número | número |"
        pattern = re.compile(r"\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*([^|]+)\|")
        
        lines = text.split('\n')
        for line in lines:
            match = pattern.search(line)
            if match:
                try:
                    step_num = int(match.group(1))
                    stack_level = int(match.group(2))
                    func_name = match.group(3).strip().replace("`", "") # Limpiar backticks markdown
                    steps.append((step_num, stack_level, func_name))
                except ValueError:
                    continue # Saltar cabeceras o líneas mal formadas
        return steps

    def animate_stack(self):
        base_x = 100
        base_y = 550
        box_height = 40
        box_width = 400
        
        def draw_step(index):
            if index >= len(self.steps):
                self.canvas.create_text(300, 30, text="Fin de la Ejecución", fill="#00ff00", font=("Arial", 16, "bold"))
                return

            step, level, func = self.steps[index]
            
            self.canvas.delete("all")
            
            # Info Superior
            self.canvas.create_text(300, 30, text=f"Paso {step}: Ejecutando...", fill="white", font=("Arial", 14, "bold"))
            self.canvas.create_text(300, 60, text=f"Función: {func}", fill="#4CA6FF", font=("Consolas", 12))
            self.canvas.create_text(300, 90, text=f"Profundidad de Pila: {level}", fill="gray", font=("Arial", 12))

            # Colores para los niveles de pila
            colors = ["#2B2B2B", "#3B8ED0", "#E04F5F", "#2CC985", "#E5B305", "#9866C9"]
            
            # Dibujar la pila
            for i in range(1, level + 1):
                color = colors[i % len(colors)]
                y1 = base_y - (i * (box_height + 5))
                y2 = y1 + box_height
                
                # Caja del Stack Frame
                self.canvas.create_rectangle(base_x, y1, base_x + box_width, y2, fill=color, outline="white", width=2)
                
                # Texto del Stack Frame
                label = f"Stack Frame #{i}"
                if i == level:
                    label += f" (Activo)"
                
                self.canvas.create_text(base_x + 200, y1 + 20, text=label, fill="white", font=("Consolas", 10, "bold"))

            self.after(800, draw_step, index + 1) # 0.8s por paso

        draw_step(0)

if __name__ == "__main__":
    app = AlgorithmAnalyzerApp()
    app.mainloop()