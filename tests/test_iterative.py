
import sys
import os

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.parsing.PseudoCodeAnalyzerLexer import PseudoCodeAnalyzerLexer
from src.parsing.PseudoCodeAnalyzerParser import PseudoCodeAnalyzerParser
from src.analysis.CostCalculator import CostCalculator
from antlr4 import InputStream, CommonTokenStream

def test_iterative_explanation():
    # Bubble Sort Example
    code = """
    BUBBLESORT(arr, n)
    begin
        for i from 1 to n do
        begin
            for j from 1 to n do
            begin
                x <- x + 1;
            end;
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
    
    print("Explanation:")
    print(result.explanation)
    
    assert result.explanation is not None
    assert "Análisis Iterativo" in result.explanation
    assert "ciclos anidados" in result.explanation or "ciclos" in result.explanation
    
    print("Test Passed!")

if __name__ == "__main__":
    test_iterative_explanation()
