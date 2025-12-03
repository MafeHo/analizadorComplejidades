import customtkinter as ctk
from tkinter import filedialog, messagebox
import threading
import sys
import os
from io import StringIO

# Importamos la lógica de tu main.py
# Asegúrate de que estás ejecutando esto desde la raíz del proyecto
from .main import analyze_algorithm

class AlgorithmAnalyzerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.title("Analizador de Complejidad Algorítmica + LLM")
        self.geometry("1100x700")
        ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
        ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

        self.current_file_path = None

        # --- Layout Principal (Grid) ---
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- Panel Izquierdo (Controles y Editor) ---
        self.left_frame = ctk.CTkFrame(self, width=400, corner_radius=0)
        self.left_frame.grid(row=0, column=0, sticky="nsew")
        self.left_frame.grid_rowconfigure(2, weight=1)

        self.logo_label = ctk.CTkLabel(self.left_frame, text="AlgoAnalyzer AI", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Botones de Archivo
        self.btn_load = ctk.CTkButton(self.left_frame, text="Cargar Algoritmo (.txt)", command=self.load_file)
        self.btn_load.grid(row=1, column=0, padx=20, pady=10)

        # Editor de Código (Solo lectura visual, editable si se desea)
        self.lbl_editor = ctk.CTkLabel(self.left_frame, text="Código Fuente:", anchor="w")
        self.lbl_editor.grid(row=2, column=0, padx=20, pady=(10, 0), sticky="w")
        
        self.code_editor = ctk.CTkTextbox(self.left_frame, width=350)
        self.code_editor.grid(row=3, column=0, padx=20, pady=(0, 20), sticky="nsew")

        # Opciones
        self.switch_translate_var = ctk.StringVar(value="off")
        self.switch_translate = ctk.CTkSwitch(self.left_frame, text="Traducir Lenguaje Natural", variable=self.switch_translate_var, onvalue="on", offvalue="off")
        self.switch_translate.grid(row=4, column=0, padx=20, pady=10)

        # Botón de Acción Principal
        self.btn_analyze = ctk.CTkButton(self.left_frame, text="EJECUTAR ANÁLISIS", fg_color="green", hover_color="darkgreen", command=self.start_analysis_thread)
        self.btn_analyze.grid(row=5, column=0, padx=20, pady=20)

        # --- Panel Derecho (Resultados) ---
        self.right_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.right_frame.grid(row=0, column=1, sticky="nsew")
        self.right_frame.grid_rowconfigure(1, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)

        # Tabview para organizar resultados
        self.tabview = ctk.CTkTabview(self.right_frame)
        self.tabview.grid(row=0, column=0, rowspan=2, padx=20, pady=20, sticky="nsew")

        self.tab_analysis = self.tabview.add("Análisis de Complejidad")
        self.tab_trace = self.tabview.add("Diagrama de Seguimiento (Trace)")
        
        # Configurar layouts de los tabs
        self.tab_analysis.grid_columnconfigure(0, weight=1)
        self.tab_analysis.grid_rowconfigure(0, weight=1)
        self.tab_trace.grid_columnconfigure(0, weight=1)
        self.tab_trace.grid_rowconfigure(0, weight=1)

        # TextBox para Análisis
        self.txt_analysis = ctk.CTkTextbox(self.tab_analysis, font=ctk.CTkFont(family="Consolas", size=14))
        self.txt_analysis.grid(row=0, column=0, sticky="nsew")

        # TextBox para Trace Table
        self.txt_trace = ctk.CTkTextbox(self.tab_trace, font=ctk.CTkFont(family="Consolas", size=12))
        self.txt_trace.grid(row=0, column=0, sticky="nsew")

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            self.current_file_path = file_path
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.code_editor.delete("0.0", "end")
                self.code_editor.insert("0.0", content)
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo leer el archivo: {e}")

    def start_analysis_thread(self):
        # Ejecutar en un hilo separado para no congelar la GUI mientras el LLM piensa
        if not self.code_editor.get("0.0", "end").strip():
            messagebox.showwarning("Advertencia", "Por favor carga un archivo o escribe código.")
            return
        
        # Guardar temporalmente lo que hay en el editor por si el usuario lo editó
        temp_path = "temp_gui_input.txt"
        with open(temp_path, "w", encoding="utf-8") as f:
            f.write(self.code_editor.get("0.0", "end"))
        
        self.current_file_path = temp_path
        
        self.btn_analyze.configure(state="disabled", text="Analizando...")
        threading.Thread(target=self.run_analysis).start()

    def run_analysis(self):
        # Capturar stdout para redirigirlo a la GUI
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()

        try:
            translate_mode = self.switch_translate_var.get() == "on"
            
            # Llamamos a la función de tu main.py
            analyze_algorithm(self.current_file_path, translate_mode=translate_mode)
            
            # Obtenemos el texto capturado
            output_text = mystdout.getvalue()
            
            # Separar la salida (esto es un hack visual simple basado en tus prints del main.py)
            # Buscamos donde empieza el Diagrama de Seguimiento
            split_marker = "--- 5. Generación de Diagrama de Seguimiento (15%) ---"
            
            if split_marker in output_text:
                parts = output_text.split(split_marker)
                analysis_part = parts[0]
                trace_part = split_marker + parts[1]
            else:
                analysis_part = output_text
                trace_part = "No se generó diagrama o hubo un error."

            # Actualizar GUI en el hilo principal
            self.after(0, lambda: self.update_ui(analysis_part, trace_part))

        except Exception as e:
            self.after(0, lambda: self.update_ui(f"ERROR CRÍTICO: {e}", ""))
        finally:
            sys.stdout = old_stdout
            self.after(0, lambda: self.btn_analyze.configure(state="normal", text="EJECUTAR ANÁLISIS"))

    def update_ui(self, analysis_text, trace_text):
        self.txt_analysis.delete("0.0", "end")
        self.txt_analysis.insert("0.0", analysis_text)
        
        self.txt_trace.delete("0.0", "end")
        self.txt_trace.insert("0.0", trace_text)

if __name__ == "__main__":
    app = AlgorithmAnalyzerApp()
    app.mainloop()