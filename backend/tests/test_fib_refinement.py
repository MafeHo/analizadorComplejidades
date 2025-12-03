
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
from sympy import symbols, simplify

def test_fib_refinement():
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
    result = calculator.visit(tree)
    
    with open("tests/test_output.txt", "w", encoding="utf-8") as f:
        f.write(result.explanation)
    
    # 1. Verify Explanation Content
    assert "Análisis de Recurrencia" in result.explanation
    assert "términos constantes" in result.explanation or "costo fijo" in result.explanation
    assert "Exponencial" in result.explanation
    assert "Phi" in result.explanation or "1.618" in result.explanation or "sqrt(5)" in result.explanation
    
    # 2. Verify Dominant Root Calculation (MathEngine direct test)
    engine = MathEngine()
    # T(n) = T(n-1) + T(n-2)
    # r^2 - r - 1 = 0
    # Roots: (1+sqrt(5))/2, (1-sqrt(5))/2
    # Dominant: (1+sqrt(5))/2
    
    # We can't easily access the internal state of the visitor's engine, 
    # but we can check the result string for the correct complexity
    assert "Theta(phi^n)" in result.worst_case or "Theta(((1 + sqrt(5))/2)^n)" in str(result.worst_case) or "Theta(1.618^n)" in str(result.worst_case)

    print("Test Passed!")

if __name__ == "__main__":
    test_fib_refinement()
