import sys
from antlr4 import FileStream, CommonTokenStream, InputStream
from src.parsing.PseudoCodeAnalyzerLexer import PseudoCodeAnalyzerLexer
from src.parsing.PseudoCodeAnalyzerParser import PseudoCodeAnalyzerParser
from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Syntax Error at line {line}:{column} - {msg}")

def debug_parse(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    input_stream = InputStream(content)
    lexer = PseudoCodeAnalyzerLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PseudoCodeAnalyzerParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(MyErrorListener())
    
    tree = parser.program()
    print("Parsing complete.")

if __name__ == "__main__":
    debug_parse(sys.argv[1])
