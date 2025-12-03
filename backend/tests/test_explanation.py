
import sys
import os

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.parsing.PseudoCodeAnalyzerLexer import PseudoCodeAnalyzerLexer
from src.parsing.PseudoCodeAnalyzerParser import PseudoCodeAnalyzerParser
from src.analysis.CostCalculator import CostCalculator
from antlr4 import InputStream, CommonTokenStream

def test_fibonacci_explanation():
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
    
    print("Explanation:")
    print(result.explanation)
    
    assert result.explanation is not None
    assert "Análisis de Recurrencia" in result.explanation
    assert "Ecuación Característica" in result.explanation
    assert "raíz dominante" in result.explanation
    
    print("Test Passed!")

if __name__ == "__main__":
    test_fibonacci_explanation()
