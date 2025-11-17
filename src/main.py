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

    # ... (dentro de main.py, justo después de analysis_result = calculator.visit(tree))

    # --- 2.1 IMPRESIÓN DEL ANÁLISIS LÍNEA POR LÍNEA (Requisito Fuente 16 y 143) ---
    if analysis_result and analysis_result.line_analysis:
        print("\n" + "="*60)
        print("--- ANÁLISIS DE COSTOS LÍNEA A LÍNEA ---")
        print(f"{'Línea':<10} | {'Costo Asignado':<40}")
        print("-" * 60)
        
        # Ordenamos por número de línea para que salga en orden
        sorted_logs = sorted(analysis_result.line_analysis, key=lambda x: x['line'])
        
        for item in sorted_logs:
            print(f"{item['line']:<10} | {item['cost']:<40}")
        print("="*60)
        
    # ... (continúa con la Fase 3 de validación)
    
    # 3. Fase de Validación (Comparación de Resultados del LLM)
    print("\n--- 3. Validación de Complejidad (Comparación) ---")
    print("  > Solicitando análisis directo del LLM para comparación...")
    llm_validation = llm_client.validate_complexity(full_pseudocode)
    
    print("\n--- 4. Resultados Finales ---")
    print(f"Costo Total de Tokens del Proyecto: {llm_client.get_total_token_cost()}")
    
    # --- COMPROBACIÓN AÑADIDA ---
    if analysis_result:
        print("\n--- Análisis Detallado del Sistema (T(n)) ---")
        print(f"Resultado Preliminar T(n): {analysis_result.worst_case}") 
    else:
        print("\n--- Análisis Detallado del Sistema (T(n)) ---")
        print("ERROR: El análisis falló. 'analysis_result' es None.")
        print("       (Esto usualmente indica un fallo total en el parsing de ANTLR).")
    # --- FIN DE LA COMPROBACIÓN ---

    print("\n--- Validación del LLM (Comparación) ---")
    print(llm_validation)

    # --- NUEVO BLOQUE: Generación de Diagrama (15%) ---
    print("\n" + "="*60)
    print("--- 5. Generación de Diagrama de Seguimiento (15%) ---")
    print("="*60)
    print(" > Solicitando al LLM una prueba de escritorio detallada...")
    
    trace_diagram = llm_client.generate_trace_table(full_pseudocode)
    
    print("\n" + trace_diagram)
    print("="*60)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python -m src.main <ruta_a_pseudocodigo.txt>")
    else:
        # Ejemplo de uso: python -m src.main tests/merge_sort.txt
        analyze_algorithm(sys.argv[1])