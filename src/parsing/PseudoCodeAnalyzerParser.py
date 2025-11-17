# Generated from src/parsing/PseudoCodeAnalyzer.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,48,266,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,4,0,33,8,0,11,0,12,0,34,1,0,1,0,1,1,1,1,1,1,1,
        1,1,1,5,1,44,8,1,10,1,12,1,47,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,
        2,3,2,57,8,2,1,2,3,2,60,8,2,1,2,1,2,1,2,1,2,3,2,66,8,2,1,2,3,2,69,
        8,2,5,2,71,8,2,10,2,12,2,74,9,2,3,2,76,8,2,1,3,1,3,1,3,1,3,1,3,5,
        3,83,8,3,10,3,12,3,86,9,3,3,3,88,8,3,1,3,1,3,1,3,1,3,1,3,5,3,95,
        8,3,10,3,12,3,98,9,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,109,
        8,4,1,4,4,4,112,8,4,11,4,12,4,113,1,4,3,4,117,8,4,1,5,1,5,1,5,5,
        5,122,8,5,10,5,12,5,125,9,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,133,8,6,
        1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,5,8,144,8,8,10,8,12,8,147,9,
        8,1,8,1,8,1,8,3,8,152,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,3,12,194,8,12,1,13,1,13,1,13,1,13,1,13,1,13,
        5,13,202,8,13,10,13,12,13,205,9,13,3,13,207,8,13,1,13,1,13,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,232,8,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,261,
        8,14,10,14,12,14,264,9,14,1,14,0,1,28,15,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,0,1,1,0,29,34,294,0,32,1,0,0,0,2,38,1,0,0,0,4,75,
        1,0,0,0,6,77,1,0,0,0,8,116,1,0,0,0,10,123,1,0,0,0,12,132,1,0,0,0,
        14,134,1,0,0,0,16,151,1,0,0,0,18,153,1,0,0,0,20,164,1,0,0,0,22,173,
        1,0,0,0,24,180,1,0,0,0,26,195,1,0,0,0,28,231,1,0,0,0,30,33,3,2,1,
        0,31,33,3,6,3,0,32,30,1,0,0,0,32,31,1,0,0,0,33,34,1,0,0,0,34,32,
        1,0,0,0,34,35,1,0,0,0,35,36,1,0,0,0,36,37,5,0,0,1,37,1,1,0,0,0,38,
        39,5,6,0,0,39,40,5,46,0,0,40,41,5,1,0,0,41,45,5,46,0,0,42,44,5,46,
        0,0,43,42,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,48,
        1,0,0,0,47,45,1,0,0,0,48,49,5,2,0,0,49,3,1,0,0,0,50,51,5,6,0,0,51,
        52,5,46,0,0,52,76,5,46,0,0,53,59,5,46,0,0,54,56,5,43,0,0,55,57,3,
        28,14,0,56,55,1,0,0,0,56,57,1,0,0,0,57,58,1,0,0,0,58,60,5,44,0,0,
        59,54,1,0,0,0,59,60,1,0,0,0,60,72,1,0,0,0,61,62,5,40,0,0,62,68,5,
        46,0,0,63,65,5,43,0,0,64,66,3,28,14,0,65,64,1,0,0,0,65,66,1,0,0,
        0,66,67,1,0,0,0,67,69,5,44,0,0,68,63,1,0,0,0,68,69,1,0,0,0,69,71,
        1,0,0,0,70,61,1,0,0,0,71,74,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,
        73,76,1,0,0,0,74,72,1,0,0,0,75,50,1,0,0,0,75,53,1,0,0,0,76,5,1,0,
        0,0,77,78,5,46,0,0,78,87,5,41,0,0,79,84,3,8,4,0,80,81,5,40,0,0,81,
        83,3,8,4,0,82,80,1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,
        0,85,88,1,0,0,0,86,84,1,0,0,0,87,79,1,0,0,0,87,88,1,0,0,0,88,89,
        1,0,0,0,89,90,5,42,0,0,90,96,5,4,0,0,91,92,3,4,2,0,92,93,5,3,0,0,
        93,95,1,0,0,0,94,91,1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,97,1,
        0,0,0,97,99,1,0,0,0,98,96,1,0,0,0,99,100,3,10,5,0,100,101,5,5,0,
        0,101,7,1,0,0,0,102,103,5,6,0,0,103,104,5,46,0,0,104,117,5,46,0,
        0,105,111,5,46,0,0,106,108,5,43,0,0,107,109,3,28,14,0,108,107,1,
        0,0,0,108,109,1,0,0,0,109,110,1,0,0,0,110,112,5,44,0,0,111,106,1,
        0,0,0,112,113,1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,117,1,
        0,0,0,115,117,5,46,0,0,116,102,1,0,0,0,116,105,1,0,0,0,116,115,1,
        0,0,0,117,9,1,0,0,0,118,119,3,12,6,0,119,120,5,3,0,0,120,122,1,0,
        0,0,121,118,1,0,0,0,122,125,1,0,0,0,123,121,1,0,0,0,123,124,1,0,
        0,0,124,11,1,0,0,0,125,123,1,0,0,0,126,133,3,14,7,0,127,133,3,18,
        9,0,128,133,3,20,10,0,129,133,3,22,11,0,130,133,3,24,12,0,131,133,
        3,26,13,0,132,126,1,0,0,0,132,127,1,0,0,0,132,128,1,0,0,0,132,129,
        1,0,0,0,132,130,1,0,0,0,132,131,1,0,0,0,133,13,1,0,0,0,134,135,3,
        16,8,0,135,136,5,18,0,0,136,137,3,28,14,0,137,15,1,0,0,0,138,145,
        5,46,0,0,139,140,5,43,0,0,140,141,3,28,14,0,141,142,5,44,0,0,142,
        144,1,0,0,0,143,139,1,0,0,0,144,147,1,0,0,0,145,143,1,0,0,0,145,
        146,1,0,0,0,146,152,1,0,0,0,147,145,1,0,0,0,148,149,5,46,0,0,149,
        150,5,28,0,0,150,152,5,46,0,0,151,138,1,0,0,0,151,148,1,0,0,0,152,
        17,1,0,0,0,153,154,5,8,0,0,154,155,5,46,0,0,155,156,5,18,0,0,156,
        157,3,28,14,0,157,158,5,9,0,0,158,159,3,28,14,0,159,160,5,16,0,0,
        160,161,5,4,0,0,161,162,3,10,5,0,162,163,5,5,0,0,163,19,1,0,0,0,
        164,165,5,10,0,0,165,166,5,41,0,0,166,167,3,28,14,0,167,168,5,42,
        0,0,168,169,5,16,0,0,169,170,5,4,0,0,170,171,3,10,5,0,171,172,5,
        5,0,0,172,21,1,0,0,0,173,174,5,11,0,0,174,175,3,10,5,0,175,176,5,
        12,0,0,176,177,5,41,0,0,177,178,3,28,14,0,178,179,5,42,0,0,179,23,
        1,0,0,0,180,181,5,13,0,0,181,182,5,41,0,0,182,183,3,28,14,0,183,
        184,5,42,0,0,184,185,5,14,0,0,185,186,5,4,0,0,186,187,3,10,5,0,187,
        193,5,5,0,0,188,189,5,15,0,0,189,190,5,4,0,0,190,191,3,10,5,0,191,
        192,5,5,0,0,192,194,1,0,0,0,193,188,1,0,0,0,193,194,1,0,0,0,194,
        25,1,0,0,0,195,196,5,17,0,0,196,197,5,46,0,0,197,206,5,41,0,0,198,
        203,3,28,14,0,199,200,5,40,0,0,200,202,3,28,14,0,201,199,1,0,0,0,
        202,205,1,0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,207,1,0,0,0,
        205,203,1,0,0,0,206,198,1,0,0,0,206,207,1,0,0,0,207,208,1,0,0,0,
        208,209,5,42,0,0,209,27,1,0,0,0,210,211,6,14,-1,0,211,212,5,26,0,
        0,212,213,3,28,14,0,213,214,5,27,0,0,214,232,1,0,0,0,215,216,5,41,
        0,0,216,217,3,28,14,0,217,218,5,42,0,0,218,232,1,0,0,0,219,220,5,
        37,0,0,220,232,3,28,14,0,221,222,5,46,0,0,222,223,5,41,0,0,223,224,
        3,28,14,0,224,225,5,42,0,0,225,232,1,0,0,0,226,232,3,16,8,0,227,
        232,5,47,0,0,228,232,5,38,0,0,229,232,5,39,0,0,230,232,5,7,0,0,231,
        210,1,0,0,0,231,215,1,0,0,0,231,219,1,0,0,0,231,221,1,0,0,0,231,
        226,1,0,0,0,231,227,1,0,0,0,231,228,1,0,0,0,231,229,1,0,0,0,231,
        230,1,0,0,0,232,262,1,0,0,0,233,234,10,9,0,0,234,235,5,22,0,0,235,
        261,3,28,14,10,236,237,10,8,0,0,237,238,5,23,0,0,238,261,3,28,14,
        9,239,240,10,7,0,0,240,241,5,24,0,0,241,261,3,28,14,8,242,243,10,
        6,0,0,243,244,5,25,0,0,244,261,3,28,14,7,245,246,10,5,0,0,246,247,
        5,20,0,0,247,261,3,28,14,6,248,249,10,4,0,0,249,250,5,21,0,0,250,
        261,3,28,14,5,251,252,10,3,0,0,252,253,7,0,0,0,253,261,3,28,14,4,
        254,255,10,2,0,0,255,256,5,35,0,0,256,261,3,28,14,3,257,258,10,1,
        0,0,258,259,5,36,0,0,259,261,3,28,14,2,260,233,1,0,0,0,260,236,1,
        0,0,0,260,239,1,0,0,0,260,242,1,0,0,0,260,245,1,0,0,0,260,248,1,
        0,0,0,260,251,1,0,0,0,260,254,1,0,0,0,260,257,1,0,0,0,261,264,1,
        0,0,0,262,260,1,0,0,0,262,263,1,0,0,0,263,29,1,0,0,0,264,262,1,0,
        0,0,25,32,34,45,56,59,65,68,72,75,84,87,96,108,113,116,123,132,145,
        151,193,203,206,231,260,262
    ]

class PseudoCodeAnalyzerParser ( Parser ):

    grammarFileName = "PseudoCodeAnalyzer.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "';'", "'begin'", "'end'", 
                     "'Clase'", "'NULL'", "'for'", "'to'", "'while'", "'repeat'", 
                     "'until'", "'If'", "'then'", "'else'", "'do'", "'CALL'", 
                     "'<-'", "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'mod'", 
                     "'div'", "'\\u00E2\\u201D\\u0152'", "'\\u00E2\\u201D\\u201D'", 
                     "'.'", "'<'", "'>'", "'\\u00E2\\u2030\\u00A4'", "'\\u00E2\\u2030\\u00A5'", 
                     "'='", "'\\u00E2\\u2030\\u00A0'", "'and'", "'or'", 
                     "'not'", "'T'", "'F'", "','", "'('", "')'", "'['", 
                     "']'", "'..'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "BEGIN", "END", "CLASS", "NULL", "FOR", "TO", "WHILE", 
                      "REPEAT", "UNTIL", "IF", "THEN", "ELSE", "DO", "CALL", 
                      "ASSIGN", "COMMENT", "OP_ADD", "OP_SUB", "OP_MUL", 
                      "OP_DIV_REAL", "OP_MOD", "OP_DIV_ENTERA", "CEIL", 
                      "FLOOR", "DOT", "OP_LT", "OP_GT", "OP_LE", "OP_GE", 
                      "OP_EQ", "OP_NE", "OP_AND", "OP_OR", "OP_NOT", "TRUE", 
                      "FALSE", "COLON", "LPAREN", "RPAREN", "LBRACKET", 
                      "RBRACKET", "RANGE", "ID", "NUMBER", "WS" ]

    RULE_program = 0
    RULE_class_declaration = 1
    RULE_local_vars_declaration = 2
    RULE_subroutine_declaration = 3
    RULE_parameter_declaration = 4
    RULE_statement_list = 5
    RULE_statement = 6
    RULE_assignment = 7
    RULE_variable = 8
    RULE_for_loop = 9
    RULE_while_loop = 10
    RULE_repeat_loop = 11
    RULE_if_statement = 12
    RULE_call_statement = 13
    RULE_expression = 14

    ruleNames =  [ "program", "class_declaration", "local_vars_declaration", 
                   "subroutine_declaration", "parameter_declaration", "statement_list", 
                   "statement", "assignment", "variable", "for_loop", "while_loop", 
                   "repeat_loop", "if_statement", "call_statement", "expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    BEGIN=4
    END=5
    CLASS=6
    NULL=7
    FOR=8
    TO=9
    WHILE=10
    REPEAT=11
    UNTIL=12
    IF=13
    THEN=14
    ELSE=15
    DO=16
    CALL=17
    ASSIGN=18
    COMMENT=19
    OP_ADD=20
    OP_SUB=21
    OP_MUL=22
    OP_DIV_REAL=23
    OP_MOD=24
    OP_DIV_ENTERA=25
    CEIL=26
    FLOOR=27
    DOT=28
    OP_LT=29
    OP_GT=30
    OP_LE=31
    OP_GE=32
    OP_EQ=33
    OP_NE=34
    OP_AND=35
    OP_OR=36
    OP_NOT=37
    TRUE=38
    FALSE=39
    COLON=40
    LPAREN=41
    RPAREN=42
    LBRACKET=43
    RBRACKET=44
    RANGE=45
    ID=46
    NUMBER=47
    WS=48

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PseudoCodeAnalyzerParser.EOF, 0)

        def class_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudoCodeAnalyzerParser.Class_declarationContext)
            else:
                return self.getTypedRuleContext(PseudoCodeAnalyzerParser.Class_declarationContext,i)


        def subroutine_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudoCodeAnalyzerParser.Subroutine_declarationContext)
            else:
                return self.getTypedRuleContext(PseudoCodeAnalyzerParser.Subroutine_declarationContext,i)


        def getRuleIndex(self):
            return PseudoCodeAnalyzerParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = PseudoCodeAnalyzerParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 30
                    self.class_declaration()
                    pass
                elif token in [46]:
                    self.state = 31
                    self.subroutine_declaration()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 34 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==6 or _la==46):
                    break

            self.state = 36
            self.match(PseudoCodeAnalyzerParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(PseudoCodeAnalyzerParser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PseudoCodeAnalyzerParser.ID)
            else:
                return self.getToken(PseudoCodeAnalyzerParser.ID, i)

        def getRuleIndex(self):
            return PseudoCodeAnalyzerParser.RULE_class_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_declaration" ):
                listener.enterClass_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_declaration" ):
                listener.exitClass_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declaration" ):
                return visitor.visitClass_declaration(self)
            else:
                return visitor.visitChildren(self)




    def class_declaration(self):

        localctx = PseudoCodeAnalyzerParser.Class_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(PseudoCodeAnalyzerParser.CLASS)
            self.state = 39
            self.match(PseudoCodeAnalyzerParser.ID)
            self.state = 40
            self.match(PseudoCodeAnalyzerParser.T__0)
            self.state = 41
            self.match(PseudoCodeAnalyzerParser.ID)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 42
                self.match(PseudoCodeAnalyzerParser.ID)
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self.match(PseudoCodeAnalyzerParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_vars_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(PseudoCodeAnalyzerParser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PseudoCodeAnalyzerParser.ID)
            else:
                return self.getToken(PseudoCodeAnalyzerParser.ID, i)

        def LBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(PseudoCodeAnalyzerParser.LBRACKET)
            else:
                return self.getToken(PseudoCodeAnalyzerParser.LBRACKET, i)

        def RBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(PseudoCodeAnalyzerParser.RBRACKET)
            else:
                return self.getToken(PseudoCodeAnalyzerParser.RBRACKET, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(PseudoCodeAnalyzerParser.COLON)
            else:
                return self.getToken(PseudoCodeAnalyzerParser.COLON, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudoCodeAnalyzerParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PseudoCodeAnalyzerParser.ExpressionContext,i)


        def getRuleIndex(self):
            return PseudoCodeAnalyzerParser.RULE_local_vars_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocal_vars_declaration" ):
                listener.enterLocal_vars_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocal_vars_declaration" ):
                listener.exitLocal_vars_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocal_vars_declaration" ):
                return visitor.visitLocal_vars_declaration(self)
            else:
                return visitor.visitChildren(self)




    def local_vars_declaration(self):

        localctx = PseudoCodeAnalyzerParser.Local_vars_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_local_vars_declaration)
        self._la = 0 # Token type
        try:
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.match(PseudoCodeAnalyzerParser.CLASS)
                self.state = 51
                self.match(PseudoCodeAnalyzerParser.ID)
                self.state = 52
                self.match(PseudoCodeAnalyzerParser.ID)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.match(PseudoCodeAnalyzerParser.ID)
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==43:
                    self.state = 54
                    self.match(PseudoCodeAnalyzerParser.LBRACKET)
                    self.state = 56
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & 214267395571840) != 0):
                        self.state = 55
                        self.expression(0)


                    self.state = 58
                    self.match(PseudoCodeAnalyzerParser.RBRACKET)


                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==40:
                    self.state = 61
                    self.match(PseudoCodeAnalyzerParser.COLON)
                    self.state = 62
                    self.match(PseudoCodeAnalyzerParser.ID)
                    self.state = 68
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==43:
                        self.state = 63
                        self.match(PseudoCodeAnalyzerParser.LBRACKET)
                        self.state = 65
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 214267395571840) != 0):
                            self.state = 64
                            self.expression(0)


                        self.state = 67
                        self.match(PseudoCodeAnalyzerParser.RBRACKET)


                    self.state = 74
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Subroutine_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PseudoCodeAnalyzerParser.ID, 0)

        def LPAREN(self):
            return self.getToken(PseudoCodeAnalyzerParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(PseudoCodeAnalyzerParser.RPAREN, 0)

        def BEGIN(self):
            return self.getToken(PseudoCodeAnalyzerParser.BEGIN, 0)

        def statement_list(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.Statement_listContext,0)


        def END(self):
            return self.getToken(PseudoCodeAnalyzerParser.END, 0)

        def parameter_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudoCodeAnalyzerParser.Parameter_declarationContext)
            else:
                return self.getTypedRuleContext(PseudoCodeAnalyzerParser.Parameter_declarationContext,i)


        def local_vars_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudoCodeAnalyzerParser.Local_vars_declarationContext)
            else:
                return self.getTypedRuleContext(PseudoCodeAnalyzerParser.Local_vars_declarationContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(PseudoCodeAnalyzerParser.COLON)
            else:
                return self.getToken(PseudoCodeAnalyzerParser.COLON, i)

        def getRuleIndex(self):
            return PseudoCodeAnalyzerParser.RULE_subroutine_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubroutine_declaration" ):
                listener.enterSubroutine_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubroutine_declaration" ):
                listener.exitSubroutine_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubroutine_declaration" ):
                return visitor.visitSubroutine_declaration(self)
            else:
                return visitor.visitChildren(self)




    def subroutine_declaration(self):

        localctx = PseudoCodeAnalyzerParser.Subroutine_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_subroutine_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(PseudoCodeAnalyzerParser.ID)
            self.state = 78
            self.match(PseudoCodeAnalyzerParser.LPAREN)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6 or _la==46:
                self.state = 79
                self.parameter_declaration()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==40:
                    self.state = 80
                    self.match(PseudoCodeAnalyzerParser.COLON)
                    self.state = 81
                    self.parameter_declaration()
                    self.state = 86
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 89
            self.match(PseudoCodeAnalyzerParser.RPAREN)
            self.state = 90
            self.match(PseudoCodeAnalyzerParser.BEGIN)
            self.state = 96
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 91
                    self.local_vars_declaration()
                    self.state = 92
                    self.match(PseudoCodeAnalyzerParser.T__2) 
                self.state = 98
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

            self.state = 99
            self.statement_list()
            self.state = 100
            self.match(PseudoCodeAnalyzerParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(PseudoCodeAnalyzerParser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PseudoCodeAnalyzerParser.ID)
            else:
                return self.getToken(PseudoCodeAnalyzerParser.ID, i)

        def LBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(PseudoCodeAnalyzerParser.LBRACKET)
            else:
                return self.getToken(PseudoCodeAnalyzerParser.LBRACKET, i)

        def RBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(PseudoCodeAnalyzerParser.RBRACKET)
            else:
                return self.getToken(PseudoCodeAnalyzerParser.RBRACKET, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudoCodeAnalyzerParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PseudoCodeAnalyzerParser.ExpressionContext,i)


        def getRuleIndex(self):
            return PseudoCodeAnalyzerParser.RULE_parameter_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter_declaration" ):
                listener.enterParameter_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter_declaration" ):
                listener.exitParameter_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_declaration" ):
                return visitor.visitParameter_declaration(self)
            else:
                return visitor.visitChildren(self)




    def parameter_declaration(self):

        localctx = PseudoCodeAnalyzerParser.Parameter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_parameter_declaration)
        self._la = 0 # Token type
        try:
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.match(PseudoCodeAnalyzerParser.CLASS)
                self.state = 103
                self.match(PseudoCodeAnalyzerParser.ID)
                self.state = 104
                self.match(PseudoCodeAnalyzerParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.match(PseudoCodeAnalyzerParser.ID)
                self.state = 111 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 106
                    self.match(PseudoCodeAnalyzerParser.LBRACKET)
                    self.state = 108
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & 214267395571840) != 0):
                        self.state = 107
                        self.expression(0)


                    self.state = 110
                    self.match(PseudoCodeAnalyzerParser.RBRACKET)
                    self.state = 113 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==43):
                        break

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 115
                self.match(PseudoCodeAnalyzerParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudoCodeAnalyzerParser.StatementContext)
            else:
                return self.getTypedRuleContext(PseudoCodeAnalyzerParser.StatementContext,i)


        def getRuleIndex(self):
            return PseudoCodeAnalyzerParser.RULE_statement_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement_list" ):
                listener.enterStatement_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement_list" ):
                listener.exitStatement_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_list" ):
                return visitor.visitStatement_list(self)
            else:
                return visitor.visitChildren(self)




    def statement_list(self):

        localctx = PseudoCodeAnalyzerParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_statement_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 70368744320256) != 0):
                self.state = 118
                self.statement()
                self.state = 119
                self.match(PseudoCodeAnalyzerParser.T__2)
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.AssignmentContext,0)


        def for_loop(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.For_loopContext,0)


        def while_loop(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.While_loopContext,0)


        def repeat_loop(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.Repeat_loopContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.If_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.Call_statementContext,0)


        def getRuleIndex(self):
            return PseudoCodeAnalyzerParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = PseudoCodeAnalyzerParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_statement)
        try:
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.assignment()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.for_loop()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 128
                self.while_loop()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 129
                self.repeat_loop()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 5)
                self.state = 130
                self.if_statement()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 6)
                self.state = 131
                self.call_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.VariableContext,0)


        def ASSIGN(self):
            return self.getToken(PseudoCodeAnalyzerParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PseudoCodeAnalyzerParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = PseudoCodeAnalyzerParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.variable()
            self.state = 135
            self.match(PseudoCodeAnalyzerParser.ASSIGN)
            self.state = 136
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PseudoCodeAnalyzerParser.ID)
            else:
                return self.getToken(PseudoCodeAnalyzerParser.ID, i)

        def LBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(PseudoCodeAnalyzerParser.LBRACKET)
            else:
                return self.getToken(PseudoCodeAnalyzerParser.LBRACKET, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudoCodeAnalyzerParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PseudoCodeAnalyzerParser.ExpressionContext,i)


        def RBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(PseudoCodeAnalyzerParser.RBRACKET)
            else:
                return self.getToken(PseudoCodeAnalyzerParser.RBRACKET, i)

        def DOT(self):
            return self.getToken(PseudoCodeAnalyzerParser.DOT, 0)

        def getRuleIndex(self):
            return PseudoCodeAnalyzerParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = PseudoCodeAnalyzerParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_variable)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.match(PseudoCodeAnalyzerParser.ID)
                self.state = 145
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 139
                        self.match(PseudoCodeAnalyzerParser.LBRACKET)
                        self.state = 140
                        self.expression(0)
                        self.state = 141
                        self.match(PseudoCodeAnalyzerParser.RBRACKET) 
                    self.state = 147
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.match(PseudoCodeAnalyzerParser.ID)
                self.state = 149
                self.match(PseudoCodeAnalyzerParser.DOT)
                self.state = 150
                self.match(PseudoCodeAnalyzerParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(PseudoCodeAnalyzerParser.FOR, 0)

        def ID(self):
            return self.getToken(PseudoCodeAnalyzerParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(PseudoCodeAnalyzerParser.ASSIGN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudoCodeAnalyzerParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PseudoCodeAnalyzerParser.ExpressionContext,i)


        def TO(self):
            return self.getToken(PseudoCodeAnalyzerParser.TO, 0)

        def DO(self):
            return self.getToken(PseudoCodeAnalyzerParser.DO, 0)

        def BEGIN(self):
            return self.getToken(PseudoCodeAnalyzerParser.BEGIN, 0)

        def statement_list(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.Statement_listContext,0)


        def END(self):
            return self.getToken(PseudoCodeAnalyzerParser.END, 0)

        def getRuleIndex(self):
            return PseudoCodeAnalyzerParser.RULE_for_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_loop" ):
                listener.enterFor_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_loop" ):
                listener.exitFor_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop" ):
                return visitor.visitFor_loop(self)
            else:
                return visitor.visitChildren(self)




    def for_loop(self):

        localctx = PseudoCodeAnalyzerParser.For_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_for_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(PseudoCodeAnalyzerParser.FOR)
            self.state = 154
            self.match(PseudoCodeAnalyzerParser.ID)
            self.state = 155
            self.match(PseudoCodeAnalyzerParser.ASSIGN)
            self.state = 156
            self.expression(0)
            self.state = 157
            self.match(PseudoCodeAnalyzerParser.TO)
            self.state = 158
            self.expression(0)
            self.state = 159
            self.match(PseudoCodeAnalyzerParser.DO)
            self.state = 160
            self.match(PseudoCodeAnalyzerParser.BEGIN)
            self.state = 161
            self.statement_list()
            self.state = 162
            self.match(PseudoCodeAnalyzerParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(PseudoCodeAnalyzerParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(PseudoCodeAnalyzerParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(PseudoCodeAnalyzerParser.RPAREN, 0)

        def DO(self):
            return self.getToken(PseudoCodeAnalyzerParser.DO, 0)

        def BEGIN(self):
            return self.getToken(PseudoCodeAnalyzerParser.BEGIN, 0)

        def statement_list(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.Statement_listContext,0)


        def END(self):
            return self.getToken(PseudoCodeAnalyzerParser.END, 0)

        def getRuleIndex(self):
            return PseudoCodeAnalyzerParser.RULE_while_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_loop" ):
                listener.enterWhile_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_loop" ):
                listener.exitWhile_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_loop" ):
                return visitor.visitWhile_loop(self)
            else:
                return visitor.visitChildren(self)




    def while_loop(self):

        localctx = PseudoCodeAnalyzerParser.While_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(PseudoCodeAnalyzerParser.WHILE)
            self.state = 165
            self.match(PseudoCodeAnalyzerParser.LPAREN)
            self.state = 166
            self.expression(0)
            self.state = 167
            self.match(PseudoCodeAnalyzerParser.RPAREN)
            self.state = 168
            self.match(PseudoCodeAnalyzerParser.DO)
            self.state = 169
            self.match(PseudoCodeAnalyzerParser.BEGIN)
            self.state = 170
            self.statement_list()
            self.state = 171
            self.match(PseudoCodeAnalyzerParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Repeat_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPEAT(self):
            return self.getToken(PseudoCodeAnalyzerParser.REPEAT, 0)

        def statement_list(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.Statement_listContext,0)


        def UNTIL(self):
            return self.getToken(PseudoCodeAnalyzerParser.UNTIL, 0)

        def LPAREN(self):
            return self.getToken(PseudoCodeAnalyzerParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(PseudoCodeAnalyzerParser.RPAREN, 0)

        def getRuleIndex(self):
            return PseudoCodeAnalyzerParser.RULE_repeat_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeat_loop" ):
                listener.enterRepeat_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeat_loop" ):
                listener.exitRepeat_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepeat_loop" ):
                return visitor.visitRepeat_loop(self)
            else:
                return visitor.visitChildren(self)




    def repeat_loop(self):

        localctx = PseudoCodeAnalyzerParser.Repeat_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_repeat_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(PseudoCodeAnalyzerParser.REPEAT)
            self.state = 174
            self.statement_list()
            self.state = 175
            self.match(PseudoCodeAnalyzerParser.UNTIL)
            self.state = 176
            self.match(PseudoCodeAnalyzerParser.LPAREN)
            self.state = 177
            self.expression(0)
            self.state = 178
            self.match(PseudoCodeAnalyzerParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(PseudoCodeAnalyzerParser.IF, 0)

        def LPAREN(self):
            return self.getToken(PseudoCodeAnalyzerParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(PseudoCodeAnalyzerParser.RPAREN, 0)

        def THEN(self):
            return self.getToken(PseudoCodeAnalyzerParser.THEN, 0)

        def BEGIN(self, i:int=None):
            if i is None:
                return self.getTokens(PseudoCodeAnalyzerParser.BEGIN)
            else:
                return self.getToken(PseudoCodeAnalyzerParser.BEGIN, i)

        def statement_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudoCodeAnalyzerParser.Statement_listContext)
            else:
                return self.getTypedRuleContext(PseudoCodeAnalyzerParser.Statement_listContext,i)


        def END(self, i:int=None):
            if i is None:
                return self.getTokens(PseudoCodeAnalyzerParser.END)
            else:
                return self.getToken(PseudoCodeAnalyzerParser.END, i)

        def ELSE(self):
            return self.getToken(PseudoCodeAnalyzerParser.ELSE, 0)

        def getRuleIndex(self):
            return PseudoCodeAnalyzerParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = PseudoCodeAnalyzerParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(PseudoCodeAnalyzerParser.IF)
            self.state = 181
            self.match(PseudoCodeAnalyzerParser.LPAREN)
            self.state = 182
            self.expression(0)
            self.state = 183
            self.match(PseudoCodeAnalyzerParser.RPAREN)
            self.state = 184
            self.match(PseudoCodeAnalyzerParser.THEN)
            self.state = 185
            self.match(PseudoCodeAnalyzerParser.BEGIN)
            self.state = 186
            self.statement_list()
            self.state = 187
            self.match(PseudoCodeAnalyzerParser.END)
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 188
                self.match(PseudoCodeAnalyzerParser.ELSE)
                self.state = 189
                self.match(PseudoCodeAnalyzerParser.BEGIN)
                self.state = 190
                self.statement_list()
                self.state = 191
                self.match(PseudoCodeAnalyzerParser.END)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CALL(self):
            return self.getToken(PseudoCodeAnalyzerParser.CALL, 0)

        def ID(self):
            return self.getToken(PseudoCodeAnalyzerParser.ID, 0)

        def LPAREN(self):
            return self.getToken(PseudoCodeAnalyzerParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(PseudoCodeAnalyzerParser.RPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudoCodeAnalyzerParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PseudoCodeAnalyzerParser.ExpressionContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(PseudoCodeAnalyzerParser.COLON)
            else:
                return self.getToken(PseudoCodeAnalyzerParser.COLON, i)

        def getRuleIndex(self):
            return PseudoCodeAnalyzerParser.RULE_call_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall_statement" ):
                listener.enterCall_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall_statement" ):
                listener.exitCall_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = PseudoCodeAnalyzerParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(PseudoCodeAnalyzerParser.CALL)
            self.state = 196
            self.match(PseudoCodeAnalyzerParser.ID)
            self.state = 197
            self.match(PseudoCodeAnalyzerParser.LPAREN)
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 214267395571840) != 0):
                self.state = 198
                self.expression(0)
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==40:
                    self.state = 199
                    self.match(PseudoCodeAnalyzerParser.COLON)
                    self.state = 200
                    self.expression(0)
                    self.state = 205
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 208
            self.match(PseudoCodeAnalyzerParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CEIL(self):
            return self.getToken(PseudoCodeAnalyzerParser.CEIL, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudoCodeAnalyzerParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PseudoCodeAnalyzerParser.ExpressionContext,i)


        def FLOOR(self):
            return self.getToken(PseudoCodeAnalyzerParser.FLOOR, 0)

        def LPAREN(self):
            return self.getToken(PseudoCodeAnalyzerParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(PseudoCodeAnalyzerParser.RPAREN, 0)

        def OP_NOT(self):
            return self.getToken(PseudoCodeAnalyzerParser.OP_NOT, 0)

        def ID(self):
            return self.getToken(PseudoCodeAnalyzerParser.ID, 0)

        def variable(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.VariableContext,0)


        def NUMBER(self):
            return self.getToken(PseudoCodeAnalyzerParser.NUMBER, 0)

        def TRUE(self):
            return self.getToken(PseudoCodeAnalyzerParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(PseudoCodeAnalyzerParser.FALSE, 0)

        def NULL(self):
            return self.getToken(PseudoCodeAnalyzerParser.NULL, 0)

        def OP_MUL(self):
            return self.getToken(PseudoCodeAnalyzerParser.OP_MUL, 0)

        def OP_DIV_REAL(self):
            return self.getToken(PseudoCodeAnalyzerParser.OP_DIV_REAL, 0)

        def OP_MOD(self):
            return self.getToken(PseudoCodeAnalyzerParser.OP_MOD, 0)

        def OP_DIV_ENTERA(self):
            return self.getToken(PseudoCodeAnalyzerParser.OP_DIV_ENTERA, 0)

        def OP_ADD(self):
            return self.getToken(PseudoCodeAnalyzerParser.OP_ADD, 0)

        def OP_SUB(self):
            return self.getToken(PseudoCodeAnalyzerParser.OP_SUB, 0)

        def OP_LE(self):
            return self.getToken(PseudoCodeAnalyzerParser.OP_LE, 0)

        def OP_GE(self):
            return self.getToken(PseudoCodeAnalyzerParser.OP_GE, 0)

        def OP_EQ(self):
            return self.getToken(PseudoCodeAnalyzerParser.OP_EQ, 0)

        def OP_NE(self):
            return self.getToken(PseudoCodeAnalyzerParser.OP_NE, 0)

        def OP_LT(self):
            return self.getToken(PseudoCodeAnalyzerParser.OP_LT, 0)

        def OP_GT(self):
            return self.getToken(PseudoCodeAnalyzerParser.OP_GT, 0)

        def OP_AND(self):
            return self.getToken(PseudoCodeAnalyzerParser.OP_AND, 0)

        def OP_OR(self):
            return self.getToken(PseudoCodeAnalyzerParser.OP_OR, 0)

        def getRuleIndex(self):
            return PseudoCodeAnalyzerParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PseudoCodeAnalyzerParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 211
                self.match(PseudoCodeAnalyzerParser.CEIL)
                self.state = 212
                self.expression(0)
                self.state = 213
                self.match(PseudoCodeAnalyzerParser.FLOOR)
                pass

            elif la_ == 2:
                self.state = 215
                self.match(PseudoCodeAnalyzerParser.LPAREN)
                self.state = 216
                self.expression(0)
                self.state = 217
                self.match(PseudoCodeAnalyzerParser.RPAREN)
                pass

            elif la_ == 3:
                self.state = 219
                self.match(PseudoCodeAnalyzerParser.OP_NOT)
                self.state = 220
                self.expression(0)
                pass

            elif la_ == 4:
                self.state = 221
                self.match(PseudoCodeAnalyzerParser.ID)
                self.state = 222
                self.match(PseudoCodeAnalyzerParser.LPAREN)
                self.state = 223
                self.expression(0)
                self.state = 224
                self.match(PseudoCodeAnalyzerParser.RPAREN)
                pass

            elif la_ == 5:
                self.state = 226
                self.variable()
                pass

            elif la_ == 6:
                self.state = 227
                self.match(PseudoCodeAnalyzerParser.NUMBER)
                pass

            elif la_ == 7:
                self.state = 228
                self.match(PseudoCodeAnalyzerParser.TRUE)
                pass

            elif la_ == 8:
                self.state = 229
                self.match(PseudoCodeAnalyzerParser.FALSE)
                pass

            elif la_ == 9:
                self.state = 230
                self.match(PseudoCodeAnalyzerParser.NULL)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 262
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 260
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        localctx = PseudoCodeAnalyzerParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 233
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 234
                        self.match(PseudoCodeAnalyzerParser.OP_MUL)
                        self.state = 235
                        self.expression(10)
                        pass

                    elif la_ == 2:
                        localctx = PseudoCodeAnalyzerParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 236
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 237
                        self.match(PseudoCodeAnalyzerParser.OP_DIV_REAL)
                        self.state = 238
                        self.expression(9)
                        pass

                    elif la_ == 3:
                        localctx = PseudoCodeAnalyzerParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 239
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 240
                        self.match(PseudoCodeAnalyzerParser.OP_MOD)
                        self.state = 241
                        self.expression(8)
                        pass

                    elif la_ == 4:
                        localctx = PseudoCodeAnalyzerParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 242
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 243
                        self.match(PseudoCodeAnalyzerParser.OP_DIV_ENTERA)
                        self.state = 244
                        self.expression(7)
                        pass

                    elif la_ == 5:
                        localctx = PseudoCodeAnalyzerParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 245
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 246
                        self.match(PseudoCodeAnalyzerParser.OP_ADD)
                        self.state = 247
                        self.expression(6)
                        pass

                    elif la_ == 6:
                        localctx = PseudoCodeAnalyzerParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 248
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 249
                        self.match(PseudoCodeAnalyzerParser.OP_SUB)
                        self.state = 250
                        self.expression(5)
                        pass

                    elif la_ == 7:
                        localctx = PseudoCodeAnalyzerParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 251
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 252
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33822867456) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 253
                        self.expression(4)
                        pass

                    elif la_ == 8:
                        localctx = PseudoCodeAnalyzerParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 254
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 255
                        self.match(PseudoCodeAnalyzerParser.OP_AND)
                        self.state = 256
                        self.expression(3)
                        pass

                    elif la_ == 9:
                        localctx = PseudoCodeAnalyzerParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 257
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 258
                        self.match(PseudoCodeAnalyzerParser.OP_OR)
                        self.state = 259
                        self.expression(2)
                        pass

             
                self.state = 264
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[14] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 1)
         




