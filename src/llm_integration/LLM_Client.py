# src/llm_integration/LLM_Client.py

import os
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError
import time

class LLMClient:
    def __init__(self):
        # Cargar la clave API del archivo .env
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY no encontrada en el archivo .env. Por favor, añádela.")
        
        try:
            # Inicializar el cliente
            self.client = genai.Client(api_key=api_key)
            self.model = 'gemini-2.5-flash' # Modelo rápido y eficiente para cálculos
            self.total_tokens_used = 0
            
            # Instrucción de sistema para guiar al LLM en su rol
            self.system_instruction = (
                "Eres un motor de cálculo matemático. Tu única tarea es resolver la expresión, sumatoria o recurrencia que se te da. Tu respuesta DEBE ser ÚNICAMENTE la solución asintótica final (ej. 'Theta(n)', 'O(n^2)', 'O(1)'). No incluyas 'Paso a paso', 'Análisis', 'Solución:', o cualquier otro texto explicativo."
            )
            
        except Exception as e:
            print(f"Error al inicializar el cliente Gemini: {e}")
            self.client = None

    def _send_prompt(self, prompt: str) -> str:
        """Función interna para enviar un prompt y registrar el uso de tokens."""
        if not self.client:
            return "ERROR: Cliente LLM no inicializado."
        
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
                config={'system_instruction': self.system_instruction}
            )
            
            # Registrar uso de tokens (Métrica requerida por el proyecto)
            usage = response.usage_metadata
            input_tokens = usage.prompt_token_count
            output_tokens = usage.candidates_token_count
            self.total_tokens_used += usage.total_token_count
            
            print(f"  > LLM Call: Input Tokens={input_tokens}, Output Tokens={output_tokens}")
            
            return response.text
            
        except APIError as e:
            return f"Error de API del LLM: {e}"
        except Exception as e:
            return f"Error desconocido al llamar al LLM: {e}"
        
    #original method commented out
    """def solve_equation(self, equation_type: str, expression: str) -> str:
        Resuelve sumatorias o recurrencias complejas (El 'trabajo duro').
        prompt = (
            f"Por favor, resuelve la siguiente {equation_type} y exprésala en "
            f"la notación de complejidad asintótica (O, Ω, Θ): \n\n{expression}"
        )
        return self._send_prompt(prompt)"""
    
    #prueba
    def solve_equation(self, equation_type: str, equation: str) -> str:
        prompt = (
            f"Actúa como un matemático experto. Resuelve esto para análisis de algoritmos:\n"
            f"Tipo: {equation_type}\n"
            f"Ecuación/Código: {equation}\n\n"
            f"Tu tarea: Dar SOLO la complejidad asintótica final simplificada (ej. Theta(n^2), O(log n)). "
            f"Sin explicaciones, solo la notación matemática."
        )
        
        # --- Lógica de Reintento (Retry Logic) ---
        max_retries = 3
        wait_time = 2 # Segundos iniciales
        
        for attempt in range(max_retries):
            try:
                response = self.client.models.generate_content(
                    model=self.model,
                    contents=prompt
                )
                
                if response.usage_metadata:
                    self.total_tokens_used += response.usage_metadata.total_token_count
                    
                return response.text.strip()
                
            except Exception as e:
                print(f"  ⚠️ Error API (Intento {attempt+1}/{max_retries}): {e}")
                if "503" in str(e) or "429" in str(e):
                    time.sleep(wait_time)
                    wait_time *= 2 # Exponential backoff (esperar el doble cada vez)
                else:
                    return f"Error: {e}"
        
        return "Error: API sobrecargada después de varios intentos."

    """def validate_complexity(self, algorithm_pseudocode: str) -> str:
        Valida la complejidad del algoritmo completo (Fase de Comparación).
        prompt = (
            "Analiza el siguiente pseudocódigo completo y dame su complejidad asintótica "
            "(O, Ω, y Θ) en función de n, junto con una justificación de las cotas fuertes. "
            "Pseudocódigo:\n\n"
            f"```pseudocode\n{algorithm_pseudocode}\n```"
        )
        return self._send_prompt(prompt)"""

    def validate_complexity(self, algorithm_pseudocode: str) -> str:
        """Valida la complejidad del algoritmo completo (Fase de Comparación)."""
        prompt = (
            "Analiza el siguiente pseudocódigo completo. "
            "1. Identifica si es iterativo o recursivo.\n"
            "2. Si es recursivo, extrae la Ecuación de Recurrencia y DIME QUÉ MÉTODO USAS para resolverla "
            "(ej. 'Usando el Teorema Maestro caso 2...', 'Usando Ecuación Característica...', 'Usando Método de Iteración...').\n"
            "3. Si es iterativo, explica las sumatorias.\n"
            "4. Dame la complejidad final (O, Ω, y Θ).\n\n"
            f"Pseudocódigo:\n```pseudocode\n{algorithm_pseudocode}\n```"
        )
        return self._send_prompt(prompt)

    def get_total_token_cost(self):
        return self.total_tokens_used


    # --- Agrega esto en src/llm_integration/LLM_Client.py ---

    def generate_trace_table(self, algorithm_pseudocode: str) -> str:
        """
        Genera una tabla de seguimiento (prueba de escritorio) paso a paso.
        Cumple con el requisito de 'Diagramas de representación' (15%).
        """
        prompt = (
            "Actúa como un profesor de análisis de algoritmos. "
            "Tu tarea es generar una 'Prueba de Escritorio' (Trace Table) detallada "
            "para el siguiente pseudocódigo.\n\n"
            "Requisitos:\n"
            "1. Usa un conjunto de datos pequeño pero representativo (ej. n=3 o un arreglo [3, 1, 2]).\n"
            "2. Crea una tabla en formato Markdown donde las columnas sean las variables del algoritmo "
            "(ej. i, j, A[], temp, etc.) y las filas sean los pasos de ejecución.\n"
            "3. Si hay recursión, muestra el nivel de la pila o el valor de retorno.\n"
            "4. Sé didáctico y claro.\n\n"
            f"Pseudocódigo:\n```\n{algorithm_pseudocode}\n```"
        )
        
        try:
            # NOTA: Usamos generate_content directamente sin la 'system_instruction' restrictiva
            # porque aquí SI queremos texto explicativo y formato rico, no solo matemáticas.
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
            )
            
            # Registrar el consumo de tokens
            if response.usage_metadata:
                self.total_tokens_used += response.usage_metadata.total_token_count
            
            return response.text
            
        except Exception as e:
            return f"Error generando el diagrama de seguimiento: {e}"
        
    # --- Agrega esto en src/llm_integration/LLM_Client.py ---

# src/llm_integration/LLM_Client.py

    def translate_to_pseudocode(self, natural_language_text: str) -> str:
        """
        Traduce descripción en lenguaje natural a pseudocódigo estructurado
        con formato estricto (Newlines y Sintaxis).
        """
        grammar_rules = (
            "Reglas de Sintaxis y FORMATO OBLIGATORIAS (Cúmplelas al 100%):\n"
            "1. CICLO FOR: La sintaxis es 'for variable <- inicio to fin do'.\n"
            "   -> ¡PROHIBIDO usar 'from'! (Incorrecto: 'for i from 1').\n"
            "   -> Usa '<-' para asignar el inicio.\n"
            "2. DEFINICIÓN: Escribe solo el nombre y parámetros. NO pongas 'Algoritmo' ni 'Function' antes.\n"
            "   -> Incorrecto: 'Algoritmo Suma(n)'\n"
            "   -> Correcto: 'Suma(n)'\n"
            "3. ESTRUCTURA: Coloca 'begin' SIEMPRE en una línea nueva.\n"
            "4. TERMINADORES: Cada sentencia simple debe terminar con punto y coma ';'.\n"
            "5. ASIGNACIÓN: Usa siempre '<-' (Ej: x <- 0;).\n"
            "6. BLOQUES: Usa 'begin' y 'end;' (No uses 'end for')."
        )

        prompt = (
            f"Actúa como un transpilador riguroso. Convierte esta descripción a tu sintaxis específica:\n"
            f"\"{natural_language_text}\"\n\n"
            f"Aplica estas reglas estrictas:\n{grammar_rules}\n\n"
            f"Salida: Solo el código."
        )

        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
            )
            
            code = response.text.replace("```pseudocode", "").replace("```", "").strip()
            
            if response.usage_metadata:
                self.total_tokens_used += response.usage_metadata.total_token_count
            
            return code
        except Exception as e:
            return f"// Error: {e}"