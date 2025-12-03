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

# --- IMPORTACIÓN ROBUSTA ---
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

# ¡¡ IMPORTANTE: DEJA SOLO ESTA LÍNEA SIN TRY/EXCEPT !!
from src.main import analyze_algorithm

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class OutputRedirector(object):
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        try:
            self.text_widget.configure(state="normal")
            self.text_widget.insert("end", string)
            self.text_widget.see("end")
            self.text_widget.configure(state="disabled")
        except: pass

    def flush(self): pass

class AlgorithmAnalyzerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Analizador de Complejidad Híbrido")
        self.geometry("1280x800")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.current_file_path = None
        self._init_ui()

    def _init_ui(self):
        # --- PANEL IZQUIERDO ---
        self.sidebar = ctk.CTkFrame(self, width=300, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        ctk.CTkLabel(self.sidebar, text="Analizador\nAlgorítmico", font=("Arial", 20, "bold")).grid(row=0, padx=20, pady=20)
        ctk.CTkButton(self.sidebar, text="Cargar Archivo", command=self.load_file).grid(row=1, padx=20, pady=10)
        
        ctk.CTkLabel(self.sidebar, text="Editor:", anchor="w").grid(row=2, padx=20, pady=(10,0))
        self.code_input = ctk.CTkTextbox(self.sidebar, width=280, height=250, font=("Consolas", 12))
        self.code_input.grid(row=3, padx=20, pady=5)
        
        default_code = """// Torres de Hanoi
HANOI(n)
begin
    If (n = 1) then
    begin
        HANOI <- 1;
    end
    else
    begin
        HANOI <- HANOI(n-1) + 1 + HANOI(n-1);
    end;
end"""
        self.code_input.insert("0.0", default_code)

        self.translate_switch = ctk.CTkSwitch(self.sidebar, text="Traducir Lenguaje Natural")
        self.translate_switch.grid(row=4, padx=20, pady=10)

        self.analyze_btn = ctk.CTkButton(self.sidebar, text="EJECUTAR ANÁLISIS", fg_color="green", hover_color="darkgreen", command=self.start_analysis)
        self.analyze_btn.grid(row=5, padx=20, pady=20)
        
        ctk.CTkButton(self.sidebar, text="Ver Pila Recursión", fg_color="#E04F5F", hover_color="#C03545", command=self.open_visualizer).grid(row=6, padx=20, pady=10)
        ctk.CTkButton(self.sidebar, text="Visualizar Árbol", fg_color="#2CC985", hover_color="#24A46D", command=self.open_tree_visualizer).grid(row=7, padx=20, pady=10)

        # --- PANEL DERECHO ---
        self.right_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.right_frame.grid(row=0, column=1, sticky="nsew")
        self.right_frame.grid_rowconfigure(1, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)

        # Gráfica
        self.plot_frame = ctk.CTkFrame(self.right_frame, height=250)
        self.plot_frame.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        # Tabs
        self.tabview = ctk.CTkTabview(self.right_frame)
        self.tabview.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        
        self.tab_resumen = self.tabview.add("Resumen Ejecutivo")
        self.tab_logs = self.tabview.add("Log Completo")
        self.tab_trace = self.tabview.add("Prueba de Escritorio")

        # Configuración Tabs
        self.txt_resumen = ctk.CTkTextbox(self.tab_resumen, font=("Arial", 14), state="disabled", wrap="word")
        self.txt_resumen.pack(expand=True, fill="both", padx=10, pady=10)
        
        self.txt_logs = ctk.CTkTextbox(self.tab_logs, font=("Consolas", 11), state="disabled")
        self.txt_logs.pack(expand=True, fill="both", padx=10, pady=10)
        
        self.txt_trace = ctk.CTkTextbox(self.tab_trace, font=("Consolas", 11), state="disabled", wrap="word")
        self.txt_trace.pack(expand=True, fill="both", padx=10, pady=10)

        self.last_analysis_data = None

    def load_file(self):
        path = filedialog.askopenfilename(filetypes=[("Text", "*.txt"), ("All", "*.*")])
        if path:
            self.current_file_path = path
            try:
                with open(path, 'r', encoding='utf-8') as f: 
                    self.code_input.delete("0.0", "end")
                    self.code_input.insert("0.0", f.read())
            except: pass

    def start_analysis(self):
        self.analyze_btn.configure(state="disabled", text="Analizando...")
        threading.Thread(target=self.run_analysis).start()

    def run_analysis(self):
        self.update_text(self.txt_logs, "")
        self.update_text(self.txt_resumen, "Calculando... Por favor espere.")
        self.update_text(self.txt_trace, "")

        code = self.code_input.get("0.0", "end").strip()
        if not code:
            self.after(0, lambda: self.analyze_btn.configure(state="normal", text="EJECUTAR ANÁLISIS"))
            return

        try:
            with open("temp_input.txt", "w", encoding="utf-8") as f: f.write(code)
        except: pass

        # Captura de stdout
        old_stdout = sys.stdout
        sys.stdout = OutputRedirector(self.txt_logs)

        try:
            translate = bool(self.translate_switch.get())
            data = analyze_algorithm("temp_input.txt", translate_mode=translate)
            
            # Actualización segura en el hilo principal
            self.after(0, lambda: self.update_results(data))
            
        except Exception as e:
            print(f"Error crítico: {e}")
            self.after(0, lambda: self.update_text(self.txt_resumen, f"Error: {e}"))
        finally:
            sys.stdout = old_stdout
            self.after(0, lambda: self.analyze_btn.configure(state="normal", text="EJECUTAR ANÁLISIS"))

    def update_text(self, widget, text):
        widget.configure(state="normal")
        widget.delete("0.0", "end")
        widget.insert("0.0", text)
        widget.configure(state="disabled")


    def update_results(self, data):
        if not data: return
        self.last_analysis_data = data

        # Obtener complejidad (prioridad a la validada, sino la calculada)
        comp_validated = data.get("complexity_validated", "")
        comp_calculated = data.get("complexity_calculated", "")
        
        # Limpieza agresiva para la gráfica (quitar texto alrededor)
        # Busca patrones como O(n), Theta(n^2), O(2^n)
        final_comp = "O(n)" # Default seguro
        
        # Intentar extraer notación matemática pura de la validada
        match = re.search(r'[OΘΩThetaOmega]+\s*\(([^)]+)\)', comp_validated)
        if match:
            final_comp = match.group(0) # ej: O(2^n)
        elif "2^n" in comp_calculated or "2**n" in comp_calculated:
            final_comp = "O(2^n)"
        
        self.plot_complexity(final_comp)
        
        # Actualizar textos
        self.update_text(self.txt_trace, data.get("trace_diagram", ""))
        
        summary = (
            f"📌 ALGORITMO: {data.get('algorithm_name')}\n"
            f"✅ COMPLEJIDAD FINAL: {final_comp}\n"
            f"🧮 Calculado (Raw): {comp_calculated}\n"
            f"🤖 Validado (LLM): {comp_validated}\n\n"
            f"📋 ANÁLISIS POR LÍNEAS:\n"
        )
        for log in data.get("line_by_line", []):
            summary += f" Línea {log['line']:<3} | {log['cost']}\n"
            
        self.update_text(self.txt_resumen, summary)


    def plot_complexity(self, complexity):
        for w in self.plot_frame.winfo_children(): w.destroy()
        
        fig, ax = plt.subplots(figsize=(5, 2.5), dpi=100)
        fig.patch.set_facecolor('#2b2b2b')
        ax.set_facecolor('#2b2b2b')
        
        x = np.linspace(1, 12, 100) # Rango más corto para exponenciales
        c_lower = complexity.lower()
        
        # Lógica de selección
        if "2^n" in c_lower or "2**n" in c_lower or "exponencial" in c_lower:
            y = 2**x
            color, label = '#FF33A8', "Exponencial O(2^n)"
        elif "n^2" in c_lower:
            y = x**2
            color, label = '#FF5733', "Cuadrática O(n^2)"
        elif "nlog" in c_lower:
            y = x * np.log2(x)
            color, label = '#33FF57', "Log-Lineal O(n log n)"
        elif "log" in c_lower:
            y = np.log2(x)
            color, label = '#33C1FF', "Logarítmica O(log n)"
        elif "1" in c_lower and "n" not in c_lower:
            y = np.ones_like(x)
            color, label = '#FFC300', "Constante O(1)"
        else:
            y = x
            color, label = '#DAF7A6', "Lineal O(n)"

        ax.plot(x, y, color=color, linewidth=2)
        ax.set_title(f"Visualización: {label}", color='white', fontsize=10)
        ax.tick_params(colors='white')
        ax.grid(True, linestyle='--', alpha=0.2)
        
        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def open_visualizer(self):
        content = self.txt_trace.get("0.0", "end")
        if not content.strip():
            messagebox.showwarning("Aviso", "Ejecuta un análisis primero.")
            return
        StackWindow(self, content)

    def open_tree_visualizer(self):
        if not self.last_analysis_data:
            messagebox.showwarning("Aviso", "Ejecuta un análisis primero.")
            return
        TreeVisualizerWindow(self, self.last_analysis_data)

class StackWindow(ctk.CTkToplevel):
    def __init__(self, parent, text):
        super().__init__(parent)
        self.title("Pila de Llamadas")
        self.geometry("500x600")
        self.canvas = ctk.CTkCanvas(self, bg="#1e1e1e")
        self.canvas.pack(fill="both", expand=True)
        
        self.steps = self.parse_steps(text)
        if self.steps: self.animate()
        else: self.canvas.create_text(250, 300, text="No se detectó tabla válida.", fill="white", font=("Arial", 14))

    def parse_steps(self, text):
        steps = []
        lines = text.split('\n')
        
        # Regex flexible: Busca números en columnas separadas por |
        # Intenta encontrar cualquier fila que tenga formato de tabla | A | B | C |
        for line in lines:
            if "|" not in line or "---" in line: continue
            
            parts = [p.strip() for p in line.split('|') if p.strip()]
            if len(parts) < 3: continue
            
            # Heurística para encontrar nivel y paso
            step_num = None
            level = None
            func = None
            
            # 1. Buscar número de paso (generalmente col 0, num pequeño < 1000)
            if parts[0].isdigit(): 
                step_num = int(parts[0])
            
            # 2. Buscar nivel (generalmente col 1 o 2, num muy pequeño < 50)
            # A veces el LLM pone el nombre de la función antes del nivel
            if parts[1].isdigit() and int(parts[1]) < 50:
                level = int(parts[1])
                func = parts[2] # Asumimos func en col 2
            elif parts[2].isdigit() and int(parts[2]) < 50:
                level = int(parts[2])
                func = parts[1] # Asumimos func en col 1
            
            # 3. Limpiar nombre de función
            if func:
                func = re.sub(r'[`*]', '', func).strip() # Quitar markdown
                
            if step_num is not None and level is not None:
                steps.append((step_num, level, func if func else f"Paso {step_num}"))
                
        return steps

    def animate(self):
        def draw(idx):
            if idx >= len(self.steps): 
                self.canvas.create_text(250, 50, text="FIN EJECUCIÓN", fill="#00ff00", font=("Arial", 16, "bold"))
                return
            
            step, level, func = self.steps[idx]
            self.canvas.delete("all")
            
            self.canvas.create_text(250, 30, text=f"Paso {step}: {func}", fill="white", font=("Arial", 14))
            
            # Dibujar pila
            base_y = 500
            box_h = 30
            for i in range(level):
                color = "#33C1FF" if i == level-1 else "#555555"
                self.canvas.create_rectangle(150, base_y - (i*box_h), 350, base_y - ((i+1)*box_h), fill=color, outline="white")
                self.canvas.create_text(250, base_y - (i*box_h) - 15, text=f"Nivel {i+1}", fill="white")
            
            self.after(800, lambda: draw(idx+1))
            
        draw(0)

class TreeVisualizerWindow(ctk.CTkToplevel):
    def __init__(self, parent, analysis_data):
        super().__init__(parent)
        self.title("Árbol de Recursión - Visualización Premium")
        self.geometry("1400x900")
        self.state("zoomed")
        
        self.analysis_data = analysis_data
        self.colors = ['#33C1FF', '#33FF57', '#FF33A8', '#FFC300', '#DAF7A6', '#FF5733']
        
        # Header
        self.header = ctk.CTkFrame(self, height=60, fg_color="#2b2b2b")
        self.header.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(self.header, text="ANÁLISIS DE RECURSIÓN", font=("Arial", 18, "bold"), text_color="#33C1FF").pack()
        self.lbl_info = ctk.CTkLabel(self.header, text="...", font=("Arial", 12), text_color="#aaaaaa")
        self.lbl_info.pack()
        
        # Canvas Frame
        self.plot_frame = ctk.CTkFrame(self, fg_color="#1e1e1e")
        self.plot_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.draw_tree()

    def draw_tree(self):
        try:
            mt_data = self.analysis_data.get("master_theorem_data", {})
            if not mt_data: mt_data = {}
            
            rec_type = mt_data.get("type", "unknown")
            
            fig, ax = plt.subplots(figsize=(12, 8), dpi=100)
            fig.patch.set_facecolor('#1e1e1e')
            ax.set_facecolor('#1e1e1e')
            ax.axis('off')
            
            # Profundidad de visualización
            max_depth = 4 
            
            # Definir límites explícitos para asegurar visibilidad
            # Expandimos a la derecha para dar espacio al texto
            # Expandimos a la izquierda para evitar recorte de ramas profundas (n-1, n-2...)
            ax.set_xlim(-20, 25) 
            ax.set_ylim(-7, 1)
            
            if rec_type == "master_theorem":
                a = int(mt_data.get("a", 1))
                b = float(mt_data.get("b", 1))
                f_n = mt_data.get("f_n", "n")
                self.lbl_info.configure(text=f"Teorema Maestro: Ramas={a} | Reducción=/{b} | Costo={f_n}")
                self._plot_recursive(ax, 0, 0, 0, max_depth, a, f"n", f_n, mode="div", param=b)
                
            elif rec_type == "characteristic_equation":
                lags = mt_data.get("lags", [1, 2])
                self.lbl_info.configure(text=f"Ecuación Característica: Lags={lags}")
                self._plot_characteristic(ax, 0, 0, 0, max_depth, lags, "n")
                
            elif rec_type == "linear_recurrence":
                a = int(mt_data.get("a", 1))
                k = mt_data.get("k", 1)
                self.lbl_info.configure(text=f"Recurrencia Lineal: Ramas={a} | Resta=-{k}")
                self._plot_recursive(ax, 0, 0, 0, max_depth, a, "n", "c", mode="sub", param=k)
                
            else:
                self.lbl_info.configure(text="Algoritmo Iterativo")
                ax.text(0, 0, "Sin Estructura Recursiva", ha='center', va='center', color='#555555', fontsize=20, fontname="Arial")

            # Línea separadora estética para los costos (Movida a la derecha: x=18)
            ax.plot([18, 18], [1, -max_depth*1.5 - 1], color='#333333', linewidth=1, linestyle='--')
            ax.text(19, 0.5, "ANÁLISIS DE COSTOS", ha='left', va='center', color='#888888', fontsize=10, fontweight='bold')

            canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill="both", expand=True)
            
        except Exception as e:
            messagebox.showerror("Error de Visualización", f"No se pudo generar el árbol:\n{e}")
            self.destroy()

    def _plot_recursive(self, ax, x, y, level, max_depth, branching_factor, label, cost_label, mode="div", param=1):
        # --- COSTOS LATERALES ---
        # Inicializar level_costs en el root
        if not hasattr(self, 'level_costs'): self.level_costs = {}
        if x == 0 and y == 0: self.level_costs = {}
            
        if level not in self.level_costs:
            color = self.colors[min(level, len(self.colors)-1)]
            # Posición del texto movida a la derecha (x=18.5)
            text_x = 18.5
            
            if mode == "sub":
                node_count = branching_factor ** level
                cost_text = f"Nivel {level}"
                detail_text = f"{node_count} nodos × {cost_label} = {node_count}{cost_label}"
                
                ax.text(text_x, y, cost_text, ha='left', va='bottom', color=color, fontsize=9, fontweight='bold')
                ax.text(text_x, y-0.3, detail_text, ha='left', va='top', color='#CCCCCC', fontsize=8)
                self.level_costs[level] = True
            elif mode == "div":
                # Lógica específica para Divide y Vencerás (Master Theorem)
                # Nivel i: a^i nodos de tamaño n/b^i
                # Costo total: a^i * f(n/b^i)
                
                node_count = branching_factor ** level
                
                # Formatear el tamaño del problema: n/b^i
                if level == 0: size_str = "n"
                else: size_str = f"n/{int(param)**level}"
                
                # Formatear el costo f(n)
                # Si f(n) es "cn", entonces f(n/b^i) es c(n/b^i)
                # Si f(n) es "c", es constante
                
                if "n" in cost_label:
                    # Asumimos f(n) = cn -> Costo nodo = c(size)
                    node_cost_str = f"c({size_str})"
                    total_cost_str = f"{node_count}c({size_str})"
                    # Simplificar si es posible (ej: 2 * c(n/2) = cn)
                    if branching_factor == param: # a = b (ej: MergeSort)
                        total_cost_str = f"cn"
                else:
                    # Asumimos f(n) = c -> Costo nodo = c
                    node_cost_str = "c"
                    total_cost_str = f"{node_count}c"
                
                cost_text = f"Nivel {level}"
                detail_text = f"{node_count} nodos × {node_cost_str}\nTotal: {total_cost_str}"
                
                ax.text(text_x, y, cost_text, ha='left', va='bottom', color=color, fontsize=9, fontweight='bold')
                ax.text(text_x, y-0.3, detail_text, ha='left', va='top', color='#CCCCCC', fontsize=8)
                self.level_costs[level] = True

        if level > max_depth: return
        
        # --- DIBUJO DEL NODO ---
        node_color = self.colors[min(level, len(self.colors)-1)]
        
        # Círculo con borde brillante
        circle_glow = plt.Circle((x, y), 0.35, color=node_color, alpha=0.3, zorder=1)
        circle_core = plt.Circle((x, y), 0.25, color=node_color, zorder=2)
        
        ax.add_patch(circle_glow)
        ax.add_patch(circle_core)
        
        # Texto del nodo (Argumento)
        # Para div: n, n/b, n/b^2...
        if mode == "div":
            if level == 0: node_label = "n"
            else: node_label = f"n/{int(param)**level}"
        else:
            node_label = label

        ax.text(x, y, node_label, ha='center', va='center', color='white', fontsize=7, fontweight='bold', zorder=3)
        
        # --- DIBUJO DE ARISTAS ---
        if level < max_depth:
            width = 6.0 / (branching_factor ** level)
            for i in range(branching_factor):
                if branching_factor == 1: offset = 0
                else: offset = (i - (branching_factor-1)/2) * width
                
                child_x = x + offset
                child_y = y - 1.5
                
                ax.plot([x, child_x], [y, child_y], color='#444444', linewidth=1, zorder=0, alpha=0.6)
                
                # Recursión
                # Para div, el label se calcula dinámicamente arriba, así que pasamos placeholder
                self._plot_recursive(ax, child_x, child_y, level + 1, max_depth, branching_factor, "", cost_label, mode, param)

    def _plot_characteristic(self, ax, x, y, level, max_depth, lags, label):
        # --- COSTOS LATERALES ---
        if not hasattr(self, 'level_costs'): self.level_costs = {}
        if x == 0 and y == 0: self.level_costs = {}
            
        if level not in self.level_costs:
            color = self.colors[min(level, len(self.colors)-1)]
            # Mover análisis de costos más a la derecha para dar espacio al árbol
            text_x = 18.5 
            
            num_children = len(lags)
            node_count_str = f"~{num_children}^{level}"
            
            cost_text = f"Nivel {level}"
            detail_text = f"{node_count_str} nodos\nCosto: c * {node_count_str}"
            
            ax.text(text_x, y, cost_text, ha='left', va='bottom', color=color, fontsize=9, fontweight='bold')
            ax.text(text_x, y-0.3, detail_text, ha='left', va='top', color='#CCCCCC', fontsize=8)
            self.level_costs[level] = True

        if level > max_depth: return
        
        # Color diferenciado para hojas (nivel máximo)
        if level == max_depth:
            node_color = '#E04F5F' # Rojo suave para hojas/casos base
        else:
            node_color = self.colors[min(level, len(self.colors)-1)]
        
        ax.add_patch(plt.Circle((x, y), 0.35, color=node_color, alpha=0.3, zorder=1))
        ax.add_patch(plt.Circle((x, y), 0.25, color=node_color, zorder=2))
        ax.text(x, y, label, ha='center', va='center', color='white', fontsize=7, fontweight='bold', zorder=3)
        
        if level < max_depth:
            num_children = len(lags)
            # Aumentar espaciado horizontal: decaimiento más lento
            # Antes: 8.0 / (1.3 ** level) -> Ahora: 10.0 / (1.2 ** level)
            width = 10.0 / (1.2 ** level) 
            
            for i, lag in enumerate(lags):
                if num_children == 1: offset = 0
                else: 
                    offset = (i - (num_children-1)/2) * width
                
                child_x = x + offset
                child_y = y - 1.5
                
                # Dibujar arista
                ax.plot([x, child_x], [y, child_y], color='#444444', linewidth=1, zorder=0, alpha=0.6)
                
                # Etiqueta de la arista (n-1, n-2)
                mid_x = (x + child_x) / 2
                mid_y = (y + child_y) / 2
                edge_label = f"n-{lag}"
                ax.text(mid_x, mid_y, edge_label, ha='center', va='center', color='#888888', fontsize=6, bbox=dict(facecolor='#1e1e1e', edgecolor='none', alpha=0.7))

                # Calcular nueva etiqueta del nodo
                if label == "n": new_label = f"n-{lag}"
                elif "n-" in label:
                    try:
                        curr = int(label.split("-")[1])
                        new_label = f"n-{curr + lag}"
                    except: new_label = "..."
                else: new_label = "..."
                
                self._plot_characteristic(ax, child_x, child_y, level + 1, max_depth, lags, new_label)

if __name__ == "__main__":
    app = AlgorithmAnalyzerApp()
    app.mainloop()
