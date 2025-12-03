# src/llm_integration/LLM_Client.py

import os
from dotenv import load_dotenv
import google.generativeai as genai
import time
import socket

class LLMClient:
    def __init__(self):
        # Cargar la clave API del archivo .env
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        
        self.total_tokens_used = 0
        self.model_name = "gemini-1.5-flash" # Default fallback
        self.model = None
        
        if not api_key:
            print("Error: GEMINI_API_KEY no encontrada en .env")
            return

        try:
            # Check connection first to avoid hanging on configure if DNS fails
            if not self._check_connection():
                print("Advertencia: Sin conexión a Internet. Modo Offline.")
                return

            genai.configure(api_key=api_key)
            
            # Selección dinámica del modelo
            available_models = []
            try:
                for m in genai.list_models():
                    if 'generateContent' in m.supported_generation_methods:
                        available_models.append(m.name)
            except Exception as e:
                print(f"Error listando modelos: {e}")

            # Priorizar gemini-1.5-flash, luego gemini-pro, luego el primero que haya
            if 'models/gemini-1.5-flash' in available_models:
                self.model_name = 'models/gemini-1.5-flash'
            elif 'models/gemini-pro' in available_models:
                self.model_name = 'models/gemini-pro'
            elif available_models:
                self.model_name = available_models[0]
            else:
                print("Advertencia: No se encontraron modelos disponibles. Intentando default.")
                self.model_name = 'gemini-1.5-flash'

            print(f"Usando modelo: {self.model_name}")
            self.model = genai.GenerativeModel(self.model_name)
            
            self.theoretical_context = (
                "Debes usar ESTRICTAMENTE los siguientes métodos según aplique:\n"
                "1. TEOREMA MAESTRO: Para T(n) = aT(n/b) + f(n). Verifica regularidad (Caso 3).\n"
                "2. ECUACIÓN CARACTERÍSTICA: Para lineales homogéneas (ej. Fibonacci T(n) = T(n-1) + T(n-2)). Hallar raíces.\n"
                "3. MÉTODO DEL ÁRBOL/ITERACIÓN: Si es 'Resta y Vencerás' (T(n) = T(n-1) + C) o irregular.\n"
                "4. SUMATORIAS: Para ciclos iterativos. Recuerda que la cabecera del FOR se ejecuta n+1 veces."
            )
        except Exception as e:
            print(f"Error al inicializar el cliente Gemini: {e}")
            self.model = None

    def _check_connection(self):
        try:
            # Intentar resolver google.com para verificar DNS/Internet
            socket.create_connection(("www.google.com", 80), timeout=2)
            return True
        except OSError:
            return False

    def _send_prompt(self, prompt: str, system_instr: str = None) -> str:
        """Función interna con lógica de reintento (Exponential Backoff)."""
        if not self._check_connection():
            return "Error: Sin conexión a Internet. (Modo Offline)"

        if not self.model:
            return "Error: Cliente LLM no configurado o API Key inválida."
        
        max_retries = 3
        wait_time = 2
        
        final_prompt = prompt
        if system_instr:
             final_prompt = f"INSTRUCCIÓN DEL SISTEMA: {system_instr}\n\n{prompt}"
        else:
             final_prompt = f"INSTRUCCIÓN DEL SISTEMA: {self.theoretical_context}\n\n{prompt}"

        for attempt in range(max_retries):
            try:
                response = self.model.generate_content(final_prompt)
                
                if hasattr(response, 'usage_metadata'):
                     self.total_tokens_used += response.usage_metadata.total_token_count
                
                return response.text.strip()
                
            except Exception as e:
                print(f"  ⚠️ Error API (Intento {attempt+1}/{max_retries}): {e}")
                if "429" in str(e) or "503" in str(e): # Rate limit o Overload
                    time.sleep(wait_time)
                    wait_time *= 2
                else:
                    return f"Error API: {e}"
        
        return "Error: API no disponible tras varios intentos."

    def solve_equation(self, equation_type: str, equation_details: str) -> str:
        """
        Resuelve la ecuación matemática pura.
        Recibe el contexto detallado desde CostCalculator.
        """
        prompt = (
            f"TIPO DE PROBLEMA: {equation_type}\n"
            f"DETALLES Y REGLAS:\n{equation_details}\n\n"
            f"SALIDA REQUERIDA:\n"
            f"Devuelve SOLAMENTE la complejidad asintótica final simplificada.\n"
            f"Formato esperado: Θ(n^2), O(log n), etc.\n"
            f"NO des explicaciones, NO muestres el paso a paso. SOLO LA NOTACIÓN FINAL."
        )
        return self._send_prompt(prompt)

    def validate_complexity(self, algorithm_pseudocode: str) -> str:
        """
        Valida el algoritmo completo (El 'Check' final).
        Aquí sí pedimos explicación para mostrar en el informe.
        """
        prompt = (
            "Analiza el siguiente pseudocódigo completo y valida su complejidad.\n"
            "1. Identifica si es Iterativo o Recursivo.\n"
            "2. Si es Recursivo: ¿Qué método teórico aplica? (Maestro, Característica, Árbol).\n"
            "3. Si es Iterativo: Identifica patrones de bucles (Sumatorias).\n"
            "4. Conclusión Final: Complejidad en Peor Caso (O), Mejor Caso (Ω) y Promedio (Θ).\n\n"
            f"CÓDIGO:\n```\n{algorithm_pseudocode}\n```"
        )
        sys_instr = "Eres un profesor evaluando un proyecto de algoritmos. Sé técnico y preciso."
        return self._send_prompt(prompt, system_instr=sys_instr)

    def generate_trace_table(self, algorithm_pseudocode: str) -> str:
        """
        Genera la tabla de seguimiento para la GUI.
        IMPORTANTE: Formato estricto separado por '|' para que gui_app.py no falle.
        """
        prompt = (
            "Genera una PRUEBA DE ESCRITORIO (Trace Table) para el siguiente código.\n"
            "Usa un caso de prueba pequeño (ej. n=3 o array=[2,1]).\n\n"
            "REQUISITO DE FORMATO CRÍTICO:\n"
            "Devuelve la tabla usando el formato Markdown con tuberías '|'.\n"
            "Las columnas DEBEN ser:\n"
            "| Paso | Nivel_Pila | Función | Variables |\n\n"
            "Donde:\n"
            "- Paso: Número entero secuencial.\n"
            "- Nivel_Pila: Número entero (1 para main, 2 para primera llamada recursiva...).\n"
            "- Función: Nombre de la función actual.\n"
            "- Variables: Estado de variables clave (ej. i=0, n=3).\n\n"
            f"CÓDIGO:\n```\n{algorithm_pseudocode}\n```"
        )
        sys_instr = "Generador de datos estructurados para visualización."
        return self._send_prompt(prompt, system_instr=sys_instr)

    def translate_to_pseudocode(self, natural_language_text: str) -> str:
        """Traduce lenguaje natural a la sintaxis del parser."""
        grammar_rules = (
            "SINTAXIS OBLIGATORIA (ANTLR G4):\n"
            "1. Asignación: usa '<-'\n"
            "2. Ciclos: 'for i <- 1 to n do begin ... end;'\n"
            "3. Condicionales: 'If (cond) then begin ... end else begin ... end;'\n"
            "4. Bloques: Siempre usa 'begin' y 'end' para cuerpos de control.\n"
            "5. Comentarios: Usa '//'\n"
            "6. Fin de línea: Usa punto y coma ';'\n"
        )
        
        prompt = (
            f"Traduce esta descripción a pseudocódigo estricto:\n"
            f"\"{natural_language_text}\"\n\n"
            f"{grammar_rules}\n"
            f"Salida: SOLO el bloque de código."
        )
        return self._send_prompt(prompt)

    def get_total_token_cost(self):
        return self.total_tokens_used