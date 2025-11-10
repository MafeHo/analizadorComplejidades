# src/llm_integration/LLM_Client.py

import os
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError

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
                "Eres un motor de cálculo especializado en resolver expresiones matemáticas, "
                "sumatorias, y relaciones de recurrencia. Tu única tarea es proporcionar "
                "la solución simplificada en notación O, Ω, o Θ, junto con el razonamiento "
                "paso a paso. No generes código. Solo resuelve el problema matemático planteado."
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

    def solve_equation(self, equation_type: str, expression: str) -> str:
        """Resuelve sumatorias o recurrencias complejas (El 'trabajo duro')."""
        prompt = (
            f"Por favor, resuelve la siguiente {equation_type} y exprésala en "
            f"la notación de complejidad asintótica (O, Ω, Θ): \n\n{expression}"
        )
        return self._send_prompt(prompt)

    def validate_complexity(self, algorithm_pseudocode: str) -> str:
        """Valida la complejidad del algoritmo completo (Fase de Comparación)."""
        prompt = (
            "Analiza el siguiente pseudocódigo completo y dame su complejidad asintótica "
            "(O, Ω, y Θ) en función de n, junto con una justificación de las cotas fuertes. "
            "Pseudocódigo:\n\n"
            f"```pseudocode\n{algorithm_pseudocode}\n```"
        )
        return self._send_prompt(prompt)

    def get_total_token_cost(self):
        return self.total_tokens_used