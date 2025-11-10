# src/main.py

import sys
from antlr4 import FileStream, CommonTokenStream
from .parsing.PseudoCodeAnalyzerLexer import PseudoCodeAnalyzerLexer
from .parsing.PseudoCodeAnalyzerParser import PseudoCodeAnalyzerParser
from .analysis.CostCalculator import CostCalculator
from .llm_integration.LLM_Client import LLMClient

def analyze_algorithm(filepath):
    # 1. Fase de Parsing
    print(f"--- 1. Analizando {filepath} (Parsing) ---")
    input_stream = FileStream(filepath, encoding='utf-8')
    lexer = PseudoCodeAnalyzerLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PseudoCodeAnalyzerParser(stream)
    
    # Obtener el árbol de sintaxis
    tree = parser.program()
    
    # Leer el pseudocódigo completo para la validación final
    with open(filepath, 'r', encoding='utf-8') as f:
        full_pseudocode = f.read()

    # 2. Fase de Análisis de Costos (Uso Asistido del LLM)
    print("\n--- 2. Calculando Costos (Análisis asistido por LLM) ---")
    llm_client = LLMClient()
    calculator = CostCalculator(llm_client)
    
    # Iniciar la visita al árbol para calcular T(n)
    analysis_result = calculator.visit(tree)
    
    # 3. Fase de Validación (Comparación de Resultados del LLM)
    print("\n--- 3. Validación de Complejidad (Comparación) ---")
    print("  > Solicitando análisis directo del LLM para comparación...")
    llm_validation = llm_client.validate_complexity(full_pseudocode)
    
    # 4. Resultados y Métricas
    print("\n--- 4. Resultados Finales ---")
    print(f"Costo Total de Tokens del Proyecto: {llm_client.get_total_token_cost()}")
    print("\n--- Análisis Detallado del Sistema (T(n)) ---")
    # Nota: Aquí se debería presentar el resultado simplificado de O, Ω, Θ del análisis.
    print(f"Resultado Preliminar T(n): {analysis_result.worst_case}") 
    
    print("\n--- Validación del LLM (Comparación) ---")
    print(llm_validation)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python -m src.main <ruta_a_pseudocodigo.txt>")
    else:
        # Ejemplo de uso: python -m src.main tests/merge_sort.txt
        analyze_algorithm(sys.argv[1])