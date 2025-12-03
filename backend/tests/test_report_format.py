
import sys
import os
import re

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.parsing.PseudoCodeAnalyzerLexer import PseudoCodeAnalyzerLexer
from src.parsing.PseudoCodeAnalyzerParser import PseudoCodeAnalyzerParser
from src.analysis.CostCalculator import CostCalculator
from src.analysis.MathEngine import MathEngine
from antlr4 import InputStream, CommonTokenStream

def test_report_format():
    # Fibonacci Example
    code = """
    Fibonacci(n)
    begin
        If (n <= 1) then
        begin
            return n;
        end
        else
        begin
            return Fibonacci(n-1) + Fibonacci(n-2);
        end;
    end
    """
    
    input_stream = InputStream(code)
    lexer = PseudoCodeAnalyzerLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PseudoCodeAnalyzerParser(stream)
    tree = parser.program()
    
    calculator = CostCalculator()
    # Visit returns complexity, but we need the side effects in calculator
    calculator.visit(tree)
    
    # Check recurrence equation format in calculator
    print(f"Recurrence Eq: {calculator.raw_equation}")
    assert "O(1)" in calculator.raw_equation
    assert "T(0)=O(1)" in calculator.raw_equation or "Base case: O(1)" in calculator.raw_equation
    
    # Simulate GUI logic for report generation
    data = {
        "recurrence_relation": calculator.raw_equation,
        "complexity_calculated": "Theta(phi^n)",
        "complexity_validated": "Theta(phi^n)",
        "case_best": "Theta(phi^n)",
        "case_average": "Theta(phi^n)",
        "case_worst": "Theta(phi^n)",
        "master_theorem_data": {
            "type": "characteristic_equation",
            "polynomial": "r^2 - r - 1",
            "roots": ["(1-sqrt(5))/2", "(1+sqrt(5))/2"],
            "dominant_root": "(1+sqrt(5))/2"
        },
        "explanation": "Detailed explanation..."
    }
    
    # Reconstruct summary string logic from gui_app.py (Clean Format)
    def clean_markdown(text):
        if not text: return ""
        text = re.sub(r'###+\s*(.+)', r'\n\1\n' + '-'*30, text)
        text = re.sub(r'##\s*(.+)', r'\n\1\n' + '='*30, text)
        text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
        text = re.sub(r'`(.+?)`', r'\1', text)
        text = re.sub(r'>\s*', '  NOTA: ', text)
        text = re.sub(r'^\s*-\s', '  • ', text, flags=re.MULTILINE)
        return text.strip()

    recurrence_eq = data.get("recurrence_relation", "N/A")
    
    mt_data = data.get("master_theorem_data", {})
    roots_info = ""
    if mt_data and mt_data.get("type") == "characteristic_equation":
        poly = mt_data.get("polynomial", "")
        roots = mt_data.get("roots", [])
        roots_str = ", ".join([str(r) for r in roots])
        roots_info = f"  • Raíces: {roots_str} (del polinomio {poly} = 0)\n"
    
    final_comp = "Theta(phi^n)"
    complexity_info = f"{final_comp}"
    if "phi" in final_comp.lower():
         complexity_info += " (con phi ≈ 1.618)"
         
    cases_info = ""
    is_recursive = "T(" in str(recurrence_eq)
    if is_recursive:
         cases_info = f"  • Todos los casos (Mejor/Promedio/Peor): {final_comp} (Exponencial)"

    summary = (
        f"📊 REPORTE EJECUTIVO DE ANÁLISIS\n"
        f"{'='*40}\n\n"
        f"1️⃣  RESUMEN DE COMPLEJIDAD\n"
        f"{'-'*40}\n"
        f"  • Complejidad Final: {complexity_info}\n"
        f"  • Ecuación:          {recurrence_eq}\n"
        f"{roots_info}\n"
        
        f"2️⃣  ANÁLISIS DE ESCENARIOS\n"
        f"{'-'*40}\n"
        f"{cases_info}\n\n"
        
        f"3️⃣  EXPLICACIÓN DETALLADA\n"
        f"{'-'*40}\n"
    )
    
    explanation = data.get("explanation")
    if explanation:
        summary += clean_markdown(explanation)
    
    print("Generated Summary:")
    print(summary)
    
    assert "📊 REPORTE EJECUTIVO DE ANÁLISIS" in summary
    assert "1️⃣  RESUMEN DE COMPLEJIDAD" in summary
    assert "  • Complejidad Final: Theta(phi^n) (con phi ≈ 1.618)" in summary
    assert "  • Raíces: (1-sqrt(5))/2, (1+sqrt(5))/2" in summary
    assert "3️⃣  EXPLICACIÓN DETALLADA" in summary
    
    print("Test Passed!")

if __name__ == "__main__":
    test_report_format()
