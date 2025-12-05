
import sys
from antlr4 import *
from src.parsing.PseudoCodeAnalyzerLexer import PseudoCodeAnalyzerLexer
from src.parsing.PseudoCodeAnalyzerParser import PseudoCodeAnalyzerParser
from src.analysis.CostCalculator import CostCalculator

code = """
BranchingAlgorithm(n)
begin
    If (n mod 2 = 0) then
    begin
        return 1;
    end
    else
    begin
        for i <- 1 to n do
        begin
            CALL print(i);
        end
    end
end
"""

def test_branching():
    input_stream = InputStream(code)
    lexer = PseudoCodeAnalyzerLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PseudoCodeAnalyzerParser(stream)
    tree = parser.program()
    
    calculator = CostCalculator()
    result = calculator.visit(tree)
    
    print(f"Worst Case: {result.worst_case}")
    print(f"Is Exact: {calculator.is_exact}")
    print(f"Line Logs: {result.line_analysis}")

if __name__ == "__main__":
    test_branching()
