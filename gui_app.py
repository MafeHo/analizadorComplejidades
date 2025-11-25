import customtkinter as ctk
import sys
import threading
from io import StringIO
from src.main import analyze_algorithm  # Importamos tu lógica existente
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import re
import time

# Configuración inicial de diseño
ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

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

        # Configuración de la ventana
        self.title("Analizador de Complejidad Híbrido (ANTLR + LLM)")
        self.geometry("1100x700")

        # Grid layout (2 columnas)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- PANEL IZQUIERDO (Entrada y Controles) ---
        self.sidebar_frame = ctk.CTkFrame(self, width=300, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Analizador\nAlgorítmico", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.code_label = ctk.CTkLabel(self.sidebar_frame, text="Escribe tu Algoritmo:", anchor="w")
        self.code_label.grid(row=1, column=0, padx=20, pady=(10, 0))

        # Caja de texto para el Código
        self.code_input = ctk.CTkTextbox(self.sidebar_frame, width=280, height=300, font=("Consolas", 12))
        self.code_input.grid(row=2, column=0, padx=20, pady=(5, 20))
        # Código de ejemplo por defecto
        default_code = """SumaGauss(n)
begin
    suma <- 0;
    for i <- 1 to n do
    begin
        suma <- suma + i;
    end;
end;"""
        self.code_input.insert("0.0", default_code)

        # Switch para traducción
        self.translate_switch = ctk.CTkSwitch(self.sidebar_frame, text="Es Lenguaje Natural (Traducir)")
        self.translate_switch.grid(row=3, column=0, padx=20, pady=10)

        # Botón de Analizar
        self.analyze_button = ctk.CTkButton(self.sidebar_frame, text="ANALYZE NOW", command=self.start_analysis_thread)
        self.analyze_button.grid(row=4, column=0, padx=20, pady=20)

        
        # Botón de Visualizar Recursión
        self.visualize_btn = ctk.CTkButton(self.sidebar_frame, text="Ver Animación Pila (Recursión)", fg_color="#E04F5F", hover_color="#C03545", command=self.open_stack_visualizer)
        self.visualize_btn.grid(row=5, column=0, padx=20, pady=10)

        # --- PANEL DERECHO (Resultados y Gráficas) ---
        self.right_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.right_frame.grid(row=0, column=1, sticky="nsew")
        self.right_frame.grid_rowconfigure(1, weight=1) # Output expandible
        self.right_frame.grid_columnconfigure(0, weight=1)

        # 1. Gráfica (Placeholder por ahora)
        self.plot_frame = ctk.CTkFrame(self.right_frame, height=200, fg_color=None)
        self.plot_frame.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        
        # Etiqueta de Consola
        self.console_label = ctk.CTkLabel(self.right_frame, text="Log de Ejecución y Análisis:", anchor="w")
        self.console_label.grid(row=1, column=0, padx=20, pady=(0,5), sticky="w")

        # 2. Consola de Salida (Donde se redirigen los prints)
        self.console_output = ctk.CTkTextbox(self.right_frame, font=("Consolas", 11), state="disabled")
        self.console_output.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="nsew")

    def open_stack_visualizer(self):
        # Obtenemos el texto actual de la consola
        console_content = self.console_output.get("0.0", "end")
        if not console_content.strip():
            return
            
        # Abrimos la ventana
        StackVisualizerWindow(self, console_content)

    def start_analysis_thread(self):
        # Ejecutamos en un hilo aparte para no congelar la interfaz
        threading.Thread(target=self.run_analysis).start()

    def run_analysis(self):
        # 1. Limpiar consola (Esto debe hacerse en el hilo principal idealmente, pero suele aguantar)
        self.console_output.configure(state="normal")
        self.console_output.delete("0.0", "end")
        self.console_output.configure(state="disabled")

        # 2. Guardar código
        code_text = self.code_input.get("0.0", "end").strip()
        if not code_text:
            return

        temp_filename = "temp_gui_input.txt"
        with open(temp_filename, "w", encoding="utf-8") as f:
            f.write(code_text)

        # 3. Redirigir stdout
        old_stdout = sys.stdout
        sys.stdout = OutputRedirector(self.console_output)

        try:
            should_translate = bool(self.translate_switch.get())
            analyze_algorithm(temp_filename, translate_mode=should_translate)
            
            # --- CORRECCIÓN AQUÍ ---
            # No llamamos a update_graph directamente. 
            # Le pedimos a Tkinter que lo haga en el hilo principal (0ms de espera).
            self.after(0, lambda: self.update_graph(code_text))

        except Exception as e:
            print(f"\nERROR CRÍTICO EN GUI: {e}")
        finally:
            sys.stdout = old_stdout
    
    def update_graph(self, code_text):
        # Esta función dibuja la gráfica en el panel superior derecho
        
        # Limpiar gráfica anterior si existe
        for widget in self.plot_frame.winfo_children():
            widget.destroy()

        # Crear figura matplotlib
        fig, ax = plt.subplots(figsize=(5, 2), dpi=100)
        fig.patch.set_facecolor('#2b2b2b') # Color de fondo oscuro
        ax.set_facecolor('#2b2b2b')
        
        # Datos dummy (Esto lo mejoraremos leyendo el resultado real del parser)
        x = np.linspace(1, 10, 100)
        
        # Heurística simple para la demo gráfica:
        if "for" in code_text and "for" in code_text.split("for")[1]: # Doble for
            y = x**2
            title = "Visualización Aproximada: Cuadrática O(n^2)"
            color = 'cyan'
        elif "for" in code_text:
            y = x
            title = "Visualización Aproximada: Lineal O(n)"
            color = 'lime'
        elif "MERGE" in code_text or "HANOI" in code_text: # Recursivo exponencial/log
             y = x * np.log(x) # Aprox
             title = "Visualización: Log-Lineal o Exponencial"
             color = 'orange'
        else:
            y = [1] * len(x)
            title = "Visualización: Constante O(1)"
            color = 'white'

        ax.plot(x, y, color=color)
        ax.set_title(title, color='white', fontsize=8)
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.grid(True, linestyle='--', alpha=0.3)

        # Insertar en Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side="top", fill="both", expand=True)


class StackVisualizerWindow(ctk.CTkToplevel):
    def __init__(self, parent, console_text):
        super().__init__(parent)
        self.title("Visualización de Pila de Llamadas (Stack Frames)")
        self.geometry("600x600")
        
        # Canvas para dibujar
        self.canvas = ctk.CTkCanvas(self, bg="#1e1e1e", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.console_text = console_text
        self.steps = self.parse_trace_table(console_text)
        
        if not self.steps:
            self.canvas.create_text(300, 300, text="No se detectó tabla de recursión en el análisis.", fill="white", font=("Arial", 14))
        else:
            self.animate_stack()

    def parse_trace_table(self, text):
        """Busca la tabla markdown en el texto y extrae (Paso, Nivel, Función)"""
        steps = []
        # Regex para buscar filas como: | 1 | 2 | FACTORIAL(2) | ...
        # Busca líneas que empiecen por | número | número | ...
        pattern = re.compile(r"\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*([^|]+)\|")
        
        lines = text.split('\n')
        for line in lines:
            match = pattern.search(line)
            if match:
                step_num = int(match.group(1))
                stack_level = int(match.group(2))
                func_name = match.group(3).strip()
                steps.append((step_num, stack_level, func_name))
        return steps

    def animate_stack(self):
        """Dibuja rectángulos basándose en el nivel de pila"""
        base_x = 100
        base_y = 550
        box_height = 40
        box_width = 400
        
        self.canvas.delete("all")
        
        def draw_step(index):
            if index >= len(self.steps):
                self.canvas.create_text(300, 30, text="Fin de la Ejecución", fill="#00ff00", font=("Arial", 16, "bold"))
                return

            step, level, func = self.steps[index]
            
            # Limpiar canvas para redibujar el estado actual
            self.canvas.delete("all")
            
            # Título
            self.canvas.create_text(300, 30, text=f"Paso {step}: {func}", fill="white", font=("Arial", 14))
            self.canvas.create_text(300, 50, text=f"Nivel de Pila: {level}", fill="gray", font=("Arial", 12))

            # Dibujar la pila (desde abajo hacia arriba)
            # Si nivel es 3, dibujamos 3 rectángulos: 1, 2, 3.
            
            colors = ["#3B8ED0", "#E04F5F", "#2CC985", "#E5B305", "#9866C9"] # Colores para diferenciar niveles
            
            for i in range(1, level + 1):
                color = colors[(i-1) % len(colors)]
                
                # Coordenadas (se apilan hacia arriba)
                y1 = base_y - (i * (box_height + 5))
                y2 = y1 + box_height
                
                # Rectángulo (Ambiente)
                self.canvas.create_rectangle(base_x, y1, base_x + box_width, y2, fill=color, outline="white")
                
                # Texto dentro del rectángulo
                # Intentamos buscar el nombre de la función de este nivel en los pasos anteriores
                # (Simplificación: usamos el nombre actual para el nivel superior)
                label = f"Stack Frame #{i}"
                if i == level:
                    label += f" : {func}"
                
                self.canvas.create_text(base_x + 200, y1 + 20, text=label, fill="black", font=("Consolas", 10, "bold"))

            # Programar el siguiente frame
            self.after(1000, draw_step, index + 1) # 1 segundo por paso

        draw_step(0)


if __name__ == "__main__":
    app = AlgorithmAnalyzerApp()
    app.mainloop()