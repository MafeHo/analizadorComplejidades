import sys
import os
from antlr4 import FileStream, CommonTokenStream, InputStream

# Imports con puntos (relativos) porque estamos dentro del paquete src
from .parsing.PseudoCodeAnalyzerLexer import PseudoCodeAnalyzerLexer
from .parsing.PseudoCodeAnalyzerParser import PseudoCodeAnalyzerParser
from .analysis.CostCalculator import CostCalculator
from .llm_integration.LLM_Client import LLMClient
import traceback
import re # Necesario para el parsing del LLM

def analyze_algorithm(filepath, translate_mode=False):
    print(f"\n{'='*60}")
    print(f"INICIANDO SISTEMA DE ANALISIS ALGORITMICO")
    print(f"{'='*60}\n")

    # Estructura por defecto
    analysis_summary = {
        "algorithm_name": "Desconocido",
        "recurrence_relation": "N/A",
        "complexity_calculated": "Desconocida",
        "complexity_validated": "Desconocida",
        "line_by_line": [],
        "trace_diagram": "No se pudo generar el diagrama.",
        "validation_details": "",
        "case_best": "N/A",
        "case_average": "N/A",
        "case_worst": "N/A"
    }

    try:
        # 0. Lectura de Archivo
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error leyendo archivo: {e}")
            return analysis_summary

        # Inicialización LLM
        try:
            llm_client = LLMClient()
        except Exception as e:
            print(f"Error conectando con LLM: {e}")
            analysis_summary["validation_details"] = f"Error de conexión: {e}"
            return analysis_summary

        full_pseudocode = content

        # Traducción (Opcional)
        if translate_mode:
            print(f"--- 0. Traducción de Lenguaje Natural ---")
            print(" > Solicitando traducción...")
            pseudocode = llm_client.translate_to_pseudocode(content)
            print("\n--- Código Generado ---\n" + pseudocode + "\n-----------------------\n")
            
            try:
                with open(filepath + ".generated.txt", 'w', encoding='utf-8') as f:
                    f.write(pseudocode)
            except: pass
            full_pseudocode = pseudocode
            analysis_summary["pseudocode"] = pseudocode # <--- ADDED THIS LINE

        # 1. Parsing ANTLR
        print(f"--- 1. Análisis Estructural (ANTLR) ---")
        input_stream = InputStream(full_pseudocode)
        lexer = PseudoCodeAnalyzerLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = PseudoCodeAnalyzerParser(stream)
        parser.removeErrorListeners()
        tree = parser.program()
        
        if parser.getNumberOfSyntaxErrors() > 0:
            print("Advertencia: Errores de sintaxis detectados (el análisis puede ser parcial).")

        # 2. Cálculo de Costos (Visitor)
        print("\n--- 2. Cálculo de Costos (Visitor) ---")
        
        # Instancia sin argumentos (MathEngine es interno)
        calculator = CostCalculator()
        
        try:
            # Esto devuelve un objeto AnalysisResult
            analysis_result = calculator.visit(tree)
            
            if analysis_result:
                # Guardar complejidad final (ej: Θ(n))
                analysis_summary["complexity_calculated"] = analysis_result.worst_case
                analysis_summary["line_by_line"] = analysis_result.line_analysis
                
                if calculator.current_algorithm_name:
                     analysis_summary["algorithm_name"] = calculator.current_algorithm_name
                
                # ### CAMBIO CLAVE AQUÍ ###
                # Usamos el atributo recurrence_eq del objeto AnalysisResult
                # Si existe, lo guardamos. Si no, es Iterativo.
                if hasattr(analysis_result, 'recurrence_eq') and analysis_result.recurrence_eq:
                     analysis_summary["recurrence_relation"] = analysis_result.recurrence_eq
                elif "T(" in str(analysis_result.worst_case): 
                     # Fallback por si acaso quedó en el worst_case
                     analysis_summary["recurrence_relation"] = analysis_result.worst_case
                else:
                     analysis_summary["recurrence_relation"] = "Algoritmo Iterativo"

                # Extraer datos del Teorema Maestro si existen
                if hasattr(analysis_result, 'master_theorem_data') and analysis_result.master_theorem_data:
                    analysis_summary["master_theorem_data"] = analysis_result.master_theorem_data
                    mt_data = analysis_result.master_theorem_data
                
                # Guardar explicacion didactica
                if hasattr(analysis_result, 'explanation') and analysis_result.explanation:
                    analysis_summary["explanation"] = analysis_result.explanation

                if hasattr(analysis_result, 'master_theorem_data') and analysis_result.master_theorem_data:
                    mt_data = analysis_result.master_theorem_data
                    print(f"\n--- DETECTOR DEL TEOREMA MAESTRO ---")
                    print(f"Tipo: {mt_data.get('type')}")
                    if mt_data.get('type') == 'master_theorem':
                        print(f" > a = {mt_data.get('a')}")
                        print(f" > b = {mt_data.get('b')}")
                        print(f" > f(n) = {mt_data.get('f_n')}")
                        print(f" > Caso Detectado: {mt_data.get('case')}")
                    elif mt_data.get('type') == 'linear_recurrence':
                        print(f" > Subtipo: {mt_data.get('subtype')}")
                        print(f" > a = {mt_data.get('a')}")
                    elif mt_data.get('type') == 'characteristic_equation':
                        print(f" > Método: Ecuación Característica")
                        print(f" > Polinomio: {mt_data.get('polynomial')} = 0")
                        print(f" > Raíces: {', '.join(mt_data.get('roots'))}")
                        print(f" > Raíz Dominante: {mt_data.get('dominant_root')}")
                    print("------------------------------------")

        except Exception as e:
            print(f"Error en Visitor: {e}")
            traceback.print_exc()

        # Imprimir log en consola
        if analysis_summary["line_by_line"]:
            print("\n--- DETALLE DE COSTOS ---")
            print(f"{'Línea':<8} | {'Costo'}")
            print("-" * 40)
            seen = set()
            for item in sorted(analysis_summary["line_by_line"], key=lambda x: x['line']):
                if item['line'] not in seen:
                    print(f"{item['line']:<8} | {item['cost']}")
                    seen.add(item['line'])
            print("="*60)

        # 3. Validación Teórica (LLM)
        print("\n--- 3. Validación Teórica (LLM) ---")
        llm_validation = llm_client.validate_complexity(full_pseudocode)
        
        # Intentar parsear JSON
        import json
        try:
            # Limpiar posibles bloques de código markdown si el LLM los puso
            clean_json = llm_validation.replace("```json", "").replace("```", "").strip()
            validation_data = json.loads(clean_json)
            
            # Extraer campos
            comp_llm = validation_data.get("complexity", "Desconocida")
            method_llm = validation_data.get("method", "N/A")
            reasoning_llm = validation_data.get("reasoning", [])
            
            # Formatear para visualización (validation_details)
            formatted_details = f"**Complejidad:** {comp_llm}\n"
            formatted_details += f"**Método:** {method_llm}\n"
            formatted_details += "**Razonamiento:**\n"
            if isinstance(reasoning_llm, list):
                for r in reasoning_llm:
                    formatted_details += f"- {r}\n"
            else:
                formatted_details += f"{reasoning_llm}\n"
            
            analysis_summary["validation_details"] = formatted_details
            
            # Usar la complejidad directa del JSON
            if "Theta" in comp_llm:
                analysis_summary["case_average"] = comp_llm
                analysis_summary["complexity_validated"] = comp_llm
            elif "O" in comp_llm:
                analysis_summary["case_worst"] = comp_llm
                if analysis_summary["complexity_validated"] == "Desconocida":
                     analysis_summary["complexity_validated"] = comp_llm
            elif "Omega" in comp_llm:
                analysis_summary["case_best"] = comp_llm

            print(f"JSON Parseado: {comp_llm} via {method_llm}")

        except json.JSONDecodeError:
            print("Advertencia: No se pudo parsear JSON del LLM. Usando texto plano.")
            analysis_summary["validation_details"] = llm_validation
            
            # Fallback a Regex (Lógica Original)
            complejidades = re.findall(r'(O|Θ|Ω|Theta|Omega)\s*\(([^)]+)\)', llm_validation)
            for tipo, valor in complejidades:
                comp_str = f"{tipo}({valor})"
                comp_str = comp_str.replace('Θ', 'Theta').replace('Ω', 'Omega')
                
                if "Theta" in comp_str:
                    analysis_summary["case_average"] = comp_str
                    analysis_summary["complexity_validated"] = comp_str
                elif "O" in tipo:
                    analysis_summary["case_worst"] = comp_str
                    if analysis_summary["complexity_validated"] == "Desconocida":
                        analysis_summary["complexity_validated"] = comp_str
                elif "Omega" in comp_str:
                    analysis_summary["case_best"] = comp_str
        
        # Si el LLM devolvió error, mostrarlo
        if "Error" in llm_validation and analysis_summary["complexity_validated"] == "Desconocida":
             analysis_summary["complexity_validated"] = llm_validation

        # Lógica de respaldo para casos (si LLM falla o es inconsistente)
        # Si tenemos una complejidad calculada y validada fuerte, usémosla
        final_comp = analysis_summary.get("complexity_validated", "Desconocida")
        if final_comp == "Desconocida" or "Error" in final_comp:
            final_comp = analysis_summary.get("complexity_calculated", "Desconocida")
            
        # Si es recursivo (detectado por T(n) o explicación), los casos suelen ser iguales
        is_recursive = "T(" in str(analysis_summary.get("recurrence_relation", ""))
        if is_recursive and final_comp != "Desconocida":
             # Sobreescribir si el LLM dio algo raro (ej: O(n) para Fibonacci)
             analysis_summary["case_best"] = final_comp
             analysis_summary["case_average"] = final_comp
             analysis_summary["case_worst"] = final_comp

        # 5. Generar Árbol de Recursión (Solo si es recursivo)
        if is_recursive:
            print("\n--- 5. Generando Árbol de Recursión ---")
            recursion_tree_json = llm_client.generate_recursion_tree(full_pseudocode)
            
            # Intentar parsear JSON para asegurar que sea válido antes de enviarlo
            try:
                import json
                clean_tree = recursion_tree_json.replace("```json", "").replace("```", "").strip()
                analysis_summary["recursion_tree"] = json.loads(clean_tree)
                print(" > Árbol generado correctamente.")
            except:
                print(" > Error parseando JSON del árbol. Se enviará como texto crudo (fallback).")
                analysis_summary["recursion_tree"] = None # O manejarlo en frontend si es null

        # 4. Diagrama de Seguimiento
        print("\n--- 4. Generando Trace Table ---")
        trace_diagram = llm_client.generate_trace_table(full_pseudocode)
        analysis_summary["trace_diagram"] = trace_diagram
        print("\nAnálisis finalizado.")

    except Exception as e:
        print(f"\nERROR GENERAL: {e}")
        traceback.print_exc()
    
    return analysis_summary

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py <archivo_pseudocodigo>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    analyze_algorithm(filepath)