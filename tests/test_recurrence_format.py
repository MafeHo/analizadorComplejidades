
import sys
import os

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.parsing.PseudoCodeAnalyzerLexer import PseudoCodeAnalyzerLexer
from src.parsing.PseudoCodeAnalyzerParser import PseudoCodeAnalyzerParser
from src.analysis.CostCalculator import CostCalculator
from antlr4 import InputStream, CommonTokenStream

def test_fibonacci_recurrence():
    file_path = os.path.join(os.path.dirname(__file__), 'FIBONACCI_TEST.txt')
    with open(file_path, 'r') as f:
        code = f.read()
    
    input_stream = InputStream(code)
    lexer = PseudoCodeAnalyzerLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PseudoCodeAnalyzerParser(stream)
    tree = parser.program()
    
    calculator = CostCalculator()
    result = calculator.visit(tree)
    
    print("Recurrence Equation:")
    print(result.recurrence_eq)
    
    # Expected format:
    # T(n) = ...
    # Base case: ... (Condition: ...)
    
    assert "Base case:" in result.recurrence_eq
    assert "Condition:" in result.recurrence_eq
    assert "n" in result.recurrence_eq and "1" in result.recurrence_eq
    # Check for base case label
    assert "Base case:" in result.recurrence_eq
    
    print("Test Passed!")

if __name__ == "__main__":
    test_fibonacci_recurrence()
