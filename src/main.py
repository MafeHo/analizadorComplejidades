# src/main.py

import sys
import os
from antlr4 import FileStream, CommonTokenStream, InputStream
from .parsing.PseudoCodeAnalyzerLexer import PseudoCodeAnalyzerLexer
from .parsing.PseudoCodeAnalyzerParser import PseudoCodeAnalyzerParser
from .analysis.CostCalculator import CostCalculator
from .llm_integration.LLM_Client import LLMClient

def analyze_algorithm(filepath, translate_mode=False):
    print(f"\n{'='*60}")
    print(f"INICIANDO SISTEMA DE ANÁLISIS ALGORÍTMICO")
    print(f"{'='*60}\n")

    # 0. Fase de Lectura y Traducción (Si aplica)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"ERROR: No se encontró el archivo '{filepath}'")
        return

    # Inicializamos el cliente LLM temprano para usarlo en traducción si es necesario
    try:
        llm_client = LLMClient()
    except Exception as e:
        print(f"ERROR CRÍTICO: No se pudo conectar con Gemini. Verifica tu API KEY. {e}")
        return

    full_pseudocode = content

    if translate_mode:
        print(f"--- 0. Traducción de Lenguaje Natural a Pseudocódigo ---")
        print(" > Detectando descripción en lenguaje natural...")
        print(" > Solicitando traducción al LLM compatible con la gramática...")
        
        pseudocode = llm_client.translate_to_pseudocode(content)
        
        print("\n--- Pseudocódigo Generado ---")
        print(pseudocode)
        print("-----------------------------\n")
        
        # Guardamos el pseudocódigo generado para referencia o depuración
        generated_path = filepath + ".generated.txt"
        with open(generated_path, 'w', encoding='utf-8') as f:
            f.write(pseudocode)
        print(f" > Pseudocódigo guardado en: {generated_path}")
        
        # Usamos el código generado para el análisis
        full_pseudocode = pseudocode

    # 1. Fase de Parsing (ANTLR)
    print(f"--- 1. Analizando Estructura (Parsing con ANTLR) ---")
    # Usamos InputStream para procesar el string directamente (sea leído o traducido)
    input_stream = InputStream(full_pseudocode)
    lexer = PseudoCodeAnalyzerLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PseudoCodeAnalyzerParser(stream)
    
    # Manejo de errores de sintaxis básico
    parser.removeErrorListeners() # Opcional: Para no ensuciar la consola si quieres manejarlo tú
    # (Pero por defecto ANTLR imprime errores a consola, lo cual es útil para depurar)
    
    tree = parser.program()
    
    if parser.getNumberOfSyntaxErrors() > 0:
        print("\n⚠️  ADVERTENCIA: Se encontraron errores de sintaxis en el pseudocódigo.")
        print("    El análisis de costos podría ser incompleto o fallar.\n")

    # 2. Fase de Análisis de Costos (Tu Sistema + LLM Calculadora)
    print("\n--- 2. Calculando Costos (Análisis Híbrido: Visitor + LLM) ---")
    calculator = CostCalculator(llm_client)
    
    try:
        analysis_result = calculator.visit(tree)
    except Exception as e:
        print(f"ERROR durante el recorrido del árbol: {e}")
        return

    # --- 2.1 IMPRESIÓN DEL ANÁLISIS LÍNEA POR LÍNEA ---
    # (Requisito Fuente 16 y 143 de los documentos)
    if analysis_result and analysis_result.line_analysis:
        print("\n" + "="*60)
        print("--- ANÁLISIS DE COSTOS LÍNEA A LÍNEA ---")
        print(f"{'Línea':<10} | {'Costo Asignado':<50}")
        print("-" * 60)
        
        # Ordenamos por número de línea
        sorted_logs = sorted(analysis_result.line_analysis, key=lambda x: x['line'])
        
        # Filtramos duplicados visuales si los hay (opcional, pero se ve más limpio)
        seen_lines = set()
        for item in sorted_logs:
            if item['line'] not in seen_lines:
                print(f"{item['line']:<10} | {item['cost']:<50}")
                seen_lines.add(item['line'])
        print("="*60)

    # 3. Fase de Validación (Comparación de Resultados del LLM)
    print("\n--- 3. Validación de Complejidad (Fase de Comparación) ---")
    print(" > Solicitando análisis teórico directo al LLM para validar tu sistema...")
    llm_validation = llm_client.validate_complexity(full_pseudocode)
    
    print("\n--- 4. Resultados Finales del Proyecto ---")
    print(f"Costo Total de Tokens (Metadatos): {llm_client.get_total_token_cost()}")
    
    if analysis_result:
        print("\n>>> Resultado de TU SISTEMA (Calculado):")
        print(f"    T(n) = {analysis_result.worst_case}") 
    else:
        print("\n>>> Resultado de TU SISTEMA:")
        print("    No se pudo determinar (Error en análisis).")

    print("\n>>> Resultado de VALIDACIÓN (Teórico LLM):")
    print(llm_validation)

    # 5. Generación de Diagrama (15% de la nota)
    print("\n" + "="*60)
    print("--- 5. Generación de Diagrama de Seguimiento (15%) ---")
    print("="*60)
    print(" > Generando Prueba de Escritorio (Trace Table) paso a paso...")
    
    trace_diagram = llm_client.generate_trace_table(full_pseudocode)
    
    print("\n" + trace_diagram)
    print("="*60)
    print("\nAnálisis completado exitosamente.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("\nUso del Analizador:")
        print("  1. Análisis normal:   python -m src.main tests/archivo.txt")
        print("  2. Traducir y analizar: python -m src.main tests/descripcion.txt --translate")
    else:
        file_path = sys.argv[1]
        # Detectar bandera de traducción
        translate = "--translate" in sys.argv
        
        analyze_algorithm(file_path, translate_mode=translate)