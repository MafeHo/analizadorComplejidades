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
        4,1,51,272,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        5,0,42,8,0,10,0,12,0,45,9,0,1,0,1,0,1,0,1,1,1,1,3,1,52,8,1,1,2,1,
        2,1,2,1,2,1,2,5,2,59,8,2,10,2,12,2,62,9,2,1,2,1,2,1,3,1,3,1,3,1,
        3,1,3,1,4,1,4,1,4,3,4,74,8,4,1,4,1,4,1,4,1,4,1,4,5,4,81,8,4,10,4,
        12,4,84,9,4,1,4,1,4,1,4,1,5,1,5,1,5,5,5,92,8,5,10,5,12,5,95,9,5,
        1,6,1,6,1,6,1,6,1,6,1,6,3,6,103,8,6,1,6,1,6,3,6,107,8,6,1,7,1,7,
        1,7,5,7,112,8,7,10,7,12,7,115,9,7,1,8,1,8,3,8,119,8,8,5,8,121,8,
        8,10,8,12,8,124,9,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,133,8,9,1,10,
        1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,4,11,144,8,11,11,11,12,11,
        145,1,11,1,11,1,11,1,11,3,11,152,8,11,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,194,8,15,1,16,1,
        16,1,16,1,16,1,16,1,16,5,16,202,8,16,10,16,12,16,205,9,16,3,16,207,
        8,16,1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,230,8,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,5,18,247,8,18,10,18,12,18,250,9,18,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,5,19,261,8,19,10,19,12,19,264,9,19,3,19,266,
        8,19,1,19,1,19,3,19,270,8,19,1,19,0,1,36,20,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,0,3,1,0,22,25,1,0,20,21,1,0,30,
        35,291,0,43,1,0,0,0,2,51,1,0,0,0,4,53,1,0,0,0,6,65,1,0,0,0,8,70,
        1,0,0,0,10,88,1,0,0,0,12,106,1,0,0,0,14,108,1,0,0,0,16,122,1,0,0,
        0,18,132,1,0,0,0,20,134,1,0,0,0,22,151,1,0,0,0,24,153,1,0,0,0,26,
        164,1,0,0,0,28,173,1,0,0,0,30,180,1,0,0,0,32,195,1,0,0,0,34,210,
        1,0,0,0,36,229,1,0,0,0,38,269,1,0,0,0,40,42,3,2,1,0,41,40,1,0,0,
        0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,46,1,0,0,0,45,43,
        1,0,0,0,46,47,3,8,4,0,47,48,5,0,0,1,48,1,1,0,0,0,49,52,3,4,2,0,50,
        52,3,6,3,0,51,49,1,0,0,0,51,50,1,0,0,0,52,3,1,0,0,0,53,54,5,6,0,
        0,54,55,5,48,0,0,55,56,5,1,0,0,56,60,5,48,0,0,57,59,5,48,0,0,58,
        57,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,63,1,0,0,
        0,62,60,1,0,0,0,63,64,5,2,0,0,64,5,1,0,0,0,65,66,5,48,0,0,66,67,
        5,44,0,0,67,68,3,36,18,0,68,69,5,45,0,0,69,7,1,0,0,0,70,71,5,48,
        0,0,71,73,5,42,0,0,72,74,3,10,5,0,73,72,1,0,0,0,73,74,1,0,0,0,74,
        75,1,0,0,0,75,76,5,43,0,0,76,82,5,4,0,0,77,78,3,14,7,0,78,79,5,3,
        0,0,79,81,1,0,0,0,80,77,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,
        1,0,0,0,83,85,1,0,0,0,84,82,1,0,0,0,85,86,3,16,8,0,86,87,5,5,0,0,
        87,9,1,0,0,0,88,93,3,12,6,0,89,90,5,41,0,0,90,92,3,12,6,0,91,89,
        1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,11,1,0,0,0,
        95,93,1,0,0,0,96,97,5,6,0,0,97,98,5,48,0,0,98,107,5,48,0,0,99,100,
        5,48,0,0,100,102,5,44,0,0,101,103,5,47,0,0,102,101,1,0,0,0,102,103,
        1,0,0,0,103,104,1,0,0,0,104,107,5,45,0,0,105,107,5,48,0,0,106,96,
        1,0,0,0,106,99,1,0,0,0,106,105,1,0,0,0,107,13,1,0,0,0,108,113,5,
        48,0,0,109,110,5,41,0,0,110,112,5,48,0,0,111,109,1,0,0,0,112,115,
        1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,15,1,0,0,0,115,113,1,
        0,0,0,116,118,3,18,9,0,117,119,5,3,0,0,118,117,1,0,0,0,118,119,1,
        0,0,0,119,121,1,0,0,0,120,116,1,0,0,0,121,124,1,0,0,0,122,120,1,
        0,0,0,122,123,1,0,0,0,123,17,1,0,0,0,124,122,1,0,0,0,125,133,3,20,
        10,0,126,133,3,24,12,0,127,133,3,26,13,0,128,133,3,28,14,0,129,133,
        3,30,15,0,130,133,3,32,16,0,131,133,3,34,17,0,132,125,1,0,0,0,132,
        126,1,0,0,0,132,127,1,0,0,0,132,128,1,0,0,0,132,129,1,0,0,0,132,
        130,1,0,0,0,132,131,1,0,0,0,133,19,1,0,0,0,134,135,3,22,11,0,135,
        136,5,19,0,0,136,137,3,36,18,0,137,21,1,0,0,0,138,143,5,48,0,0,139,
        140,5,44,0,0,140,141,3,36,18,0,141,142,5,45,0,0,142,144,1,0,0,0,
        143,139,1,0,0,0,144,145,1,0,0,0,145,143,1,0,0,0,145,146,1,0,0,0,
        146,152,1,0,0,0,147,148,5,48,0,0,148,149,5,46,0,0,149,152,5,48,0,
        0,150,152,5,48,0,0,151,138,1,0,0,0,151,147,1,0,0,0,151,150,1,0,0,
        0,152,23,1,0,0,0,153,154,5,8,0,0,154,155,5,48,0,0,155,156,5,19,0,
        0,156,157,3,36,18,0,157,158,5,9,0,0,158,159,3,36,18,0,159,160,5,
        16,0,0,160,161,5,4,0,0,161,162,3,16,8,0,162,163,5,5,0,0,163,25,1,
        0,0,0,164,165,5,10,0,0,165,166,5,42,0,0,166,167,3,36,18,0,167,168,
        5,43,0,0,168,169,5,16,0,0,169,170,5,4,0,0,170,171,3,16,8,0,171,172,
        5,5,0,0,172,27,1,0,0,0,173,174,5,11,0,0,174,175,3,16,8,0,175,176,
        5,12,0,0,176,177,5,42,0,0,177,178,3,36,18,0,178,179,5,43,0,0,179,
        29,1,0,0,0,180,181,5,13,0,0,181,182,5,42,0,0,182,183,3,36,18,0,183,
        184,5,43,0,0,184,185,5,14,0,0,185,186,5,4,0,0,186,187,3,16,8,0,187,
        193,5,5,0,0,188,189,5,15,0,0,189,190,5,4,0,0,190,191,3,16,8,0,191,
        192,5,5,0,0,192,194,1,0,0,0,193,188,1,0,0,0,193,194,1,0,0,0,194,
        31,1,0,0,0,195,196,5,17,0,0,196,197,5,48,0,0,197,206,5,42,0,0,198,
        203,3,36,18,0,199,200,5,41,0,0,200,202,3,36,18,0,201,199,1,0,0,0,
        202,205,1,0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,207,1,0,0,0,
        205,203,1,0,0,0,206,198,1,0,0,0,206,207,1,0,0,0,207,208,1,0,0,0,
        208,209,5,43,0,0,209,33,1,0,0,0,210,211,5,18,0,0,211,212,3,36,18,
        0,212,35,1,0,0,0,213,214,6,18,-1,0,214,215,5,42,0,0,215,216,3,36,
        18,0,216,217,5,43,0,0,217,230,1,0,0,0,218,219,5,26,0,0,219,220,3,
        36,18,0,220,221,5,27,0,0,221,230,1,0,0,0,222,223,5,28,0,0,223,224,
        3,36,18,0,224,225,5,29,0,0,225,230,1,0,0,0,226,227,5,38,0,0,227,
        230,3,36,18,7,228,230,3,38,19,0,229,213,1,0,0,0,229,218,1,0,0,0,
        229,222,1,0,0,0,229,226,1,0,0,0,229,228,1,0,0,0,230,248,1,0,0,0,
        231,232,10,6,0,0,232,233,7,0,0,0,233,247,3,36,18,7,234,235,10,5,
        0,0,235,236,7,1,0,0,236,247,3,36,18,6,237,238,10,4,0,0,238,239,7,
        2,0,0,239,247,3,36,18,5,240,241,10,3,0,0,241,242,5,36,0,0,242,247,
        3,36,18,4,243,244,10,2,0,0,244,245,5,37,0,0,245,247,3,36,18,3,246,
        231,1,0,0,0,246,234,1,0,0,0,246,237,1,0,0,0,246,240,1,0,0,0,246,
        243,1,0,0,0,247,250,1,0,0,0,248,246,1,0,0,0,248,249,1,0,0,0,249,
        37,1,0,0,0,250,248,1,0,0,0,251,270,5,49,0,0,252,270,5,39,0,0,253,
        270,5,40,0,0,254,270,5,7,0,0,255,256,5,48,0,0,256,265,5,42,0,0,257,
        262,3,36,18,0,258,259,5,41,0,0,259,261,3,36,18,0,260,258,1,0,0,0,
        261,264,1,0,0,0,262,260,1,0,0,0,262,263,1,0,0,0,263,266,1,0,0,0,
        264,262,1,0,0,0,265,257,1,0,0,0,265,266,1,0,0,0,266,267,1,0,0,0,
        267,270,5,43,0,0,268,270,3,22,11,0,269,251,1,0,0,0,269,252,1,0,0,
        0,269,253,1,0,0,0,269,254,1,0,0,0,269,255,1,0,0,0,269,268,1,0,0,
        0,270,39,1,0,0,0,23,43,51,60,73,82,93,102,106,113,118,122,132,145,
        151,193,203,206,229,246,248,262,265,269
    ]

class PseudoCodeAnalyzerParser ( Parser ):

    grammarFileName = "PseudoCodeAnalyzer.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "';'", "'begin'", "'end'", 
                     "'Clase'", "'NULL'", "'for'", "'to'", "'while'", "'repeat'", 
                     "'until'", "'If'", "'then'", "'else'", "'do'", "'CALL'", 
                     "<INVALID>", "'<-'", "'+'", "'-'", "'*'", "'/'", "'mod'", 
                     "'div'", "'\\u250C'", "'\\u2510'", "'\\u2514'", "'\\u2518'", 
                     "'<'", "'>'", "<INVALID>", "<INVALID>", "'='", "<INVALID>", 
                     "'and'", "'or'", "'not'", "'T'", "'F'", "','", "'('", 
                     "')'", "'['", "']'", "'.'", "'..'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "BEGIN", "END", "CLASS", "NULL", "FOR", "TO", "WHILE", 
                      "REPEAT", "UNTIL", "IF", "THEN", "ELSE", "DO", "CALL", 
                      "RETURN", "ASSIGN", "OP_ADD", "OP_SUB", "OP_MUL", 
                      "OP_DIV_REAL", "OP_MOD", "OP_DIV_INT", "CEIL", "CEIL_CLOSE", 
                      "FLOOR", "FLOOR_CLOSE", "OP_LT", "OP_GT", "OP_LE", 
                      "OP_GE", "OP_EQ", "OP_NE", "OP_AND", "OP_OR", "OP_NOT", 
                      "TRUE", "FALSE", "COLON", "LPAREN", "RPAREN", "LBRACKET", 
                      "RBRACKET", "DOT", "RANGE", "ID", "NUMBER", "WS", 
                      "COMMENT" ]

    RULE_program = 0
    RULE_structure_definition = 1
    RULE_class_definition = 2
    RULE_array_definition = 3
    RULE_algorithm_definition = 4
    RULE_param_list = 5
    RULE_parameter = 6
    RULE_local_var_decl = 7
    RULE_statement_list = 8
    RULE_statement = 9
    RULE_assignment = 10
    RULE_target_var = 11
    RULE_for_loop = 12
    RULE_while_loop = 13
    RULE_repeat_loop = 14
    RULE_if_statement = 15
    RULE_call_statement = 16
    RULE_return_statement = 17
    RULE_expression = 18
    RULE_atom = 19

    ruleNames =  [ "program", "structure_definition", "class_definition", 
                   "array_definition", "algorithm_definition", "param_list", 
                   "parameter", "local_var_decl", "statement_list", "statement", 
                   "assignment", "target_var", "for_loop", "while_loop", 
                   "repeat_loop", "if_statement", "call_statement", "return_statement", 
                   "expression", "atom" ]

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
    RETURN=18
    ASSIGN=19
    OP_ADD=20
    OP_SUB=21
    OP_MUL=22
    OP_DIV_REAL=23
    OP_MOD=24
    OP_DIV_INT=25
    CEIL=26
    CEIL_CLOSE=27
    FLOOR=28
    FLOOR_CLOSE=29
    OP_LT=30
    OP_GT=31
    OP_LE=32
    OP_GE=33
    OP_EQ=34
    OP_NE=35
    OP_AND=36
    OP_OR=37
    OP_NOT=38
    TRUE=39
    FALSE=40
    COLON=41
    LPAREN=42
    RPAREN=43
    LBRACKET=44
    RBRACKET=45
    DOT=46
    RANGE=47
    ID=48
    NUMBER=49
    WS=50
    COMMENT=51

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

        def algorithm_definition(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.Algorithm_definitionContext,0)


        def EOF(self):
            return self.getToken(PseudoCodeAnalyzerParser.EOF, 0)

        def structure_definition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudoCodeAnalyzerParser.Structure_definitionContext)
            else:
                return self.getTypedRuleContext(PseudoCodeAnalyzerParser.Structure_definitionContext,i)


        def getRuleIndex(self):
            return PseudoCodeAnalyzerParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = PseudoCodeAnalyzerParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 40
                    self.structure_definition() 
                self.state = 45
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 46
            self.algorithm_definition()
            self.state = 47
            self.match(PseudoCodeAnalyzerParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Structure_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_definition(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.Class_definitionContext,0)


        def array_definition(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.Array_definitionContext,0)


        def getRuleIndex(self):
            return PseudoCodeAnalyzerParser.RULE_structure_definition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructure_definition" ):
                return visitor.visitStructure_definition(self)
            else:
                return visitor.visitChildren(self)




    def structure_definition(self):

        localctx = PseudoCodeAnalyzerParser.Structure_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_structure_definition)
        try:
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.class_definition()
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.array_definition()
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


    class Class_definitionContext(ParserRuleContext):
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
            return PseudoCodeAnalyzerParser.RULE_class_definition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_definition" ):
                return visitor.visitClass_definition(self)
            else:
                return visitor.visitChildren(self)




    def class_definition(self):

        localctx = PseudoCodeAnalyzerParser.Class_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(PseudoCodeAnalyzerParser.CLASS)
            self.state = 54
            self.match(PseudoCodeAnalyzerParser.ID)
            self.state = 55
            self.match(PseudoCodeAnalyzerParser.T__0)
            self.state = 56
            self.match(PseudoCodeAnalyzerParser.ID)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 57
                self.match(PseudoCodeAnalyzerParser.ID)
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 63
            self.match(PseudoCodeAnalyzerParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PseudoCodeAnalyzerParser.ID, 0)

        def LBRACKET(self):
            return self.getToken(PseudoCodeAnalyzerParser.LBRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.ExpressionContext,0)


        def RBRACKET(self):
            return self.getToken(PseudoCodeAnalyzerParser.RBRACKET, 0)

        def getRuleIndex(self):
            return PseudoCodeAnalyzerParser.RULE_array_definition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_definition" ):
                return visitor.visitArray_definition(self)
            else:
                return visitor.visitChildren(self)




    def array_definition(self):

        localctx = PseudoCodeAnalyzerParser.Array_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_array_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(PseudoCodeAnalyzerParser.ID)
            self.state = 66
            self.match(PseudoCodeAnalyzerParser.LBRACKET)
            self.state = 67
            self.expression(0)
            self.state = 68
            self.match(PseudoCodeAnalyzerParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Algorithm_definitionContext(ParserRuleContext):
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

        def param_list(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.Param_listContext,0)


        def local_var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudoCodeAnalyzerParser.Local_var_declContext)
            else:
                return self.getTypedRuleContext(PseudoCodeAnalyzerParser.Local_var_declContext,i)


        def getRuleIndex(self):
            return PseudoCodeAnalyzerParser.RULE_algorithm_definition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlgorithm_definition" ):
                return visitor.visitAlgorithm_definition(self)
            else:
                return visitor.visitChildren(self)




    def algorithm_definition(self):

        localctx = PseudoCodeAnalyzerParser.Algorithm_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_algorithm_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(PseudoCodeAnalyzerParser.ID)
            self.state = 71
            self.match(PseudoCodeAnalyzerParser.LPAREN)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6 or _la==48:
                self.state = 72
                self.param_list()


            self.state = 75
            self.match(PseudoCodeAnalyzerParser.RPAREN)
            self.state = 76
            self.match(PseudoCodeAnalyzerParser.BEGIN)
            self.state = 82
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 77
                    self.local_var_decl()
                    self.state = 78
                    self.match(PseudoCodeAnalyzerParser.T__2) 
                self.state = 84
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 85
            self.statement_list()
            self.state = 86
            self.match(PseudoCodeAnalyzerParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudoCodeAnalyzerParser.ParameterContext)
            else:
                return self.getTypedRuleContext(PseudoCodeAnalyzerParser.ParameterContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(PseudoCodeAnalyzerParser.COLON)
            else:
                return self.getToken(PseudoCodeAnalyzerParser.COLON, i)

        def getRuleIndex(self):
            return PseudoCodeAnalyzerParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = PseudoCodeAnalyzerParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.parameter()
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 89
                self.match(PseudoCodeAnalyzerParser.COLON)
                self.state = 90
                self.parameter()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PseudoCodeAnalyzerParser.RULE_parameter

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParamArrayContext(ParameterContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PseudoCodeAnalyzerParser.ParameterContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(PseudoCodeAnalyzerParser.ID, 0)
        def LBRACKET(self):
            return self.getToken(PseudoCodeAnalyzerParser.LBRACKET, 0)
        def RBRACKET(self):
            return self.getToken(PseudoCodeAnalyzerParser.RBRACKET, 0)
        def RANGE(self):
            return self.getToken(PseudoCodeAnalyzerParser.RANGE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamArray" ):
                return visitor.visitParamArray(self)
            else:
                return visitor.visitChildren(self)


    class ParamSimpleContext(ParameterContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PseudoCodeAnalyzerParser.ParameterContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(PseudoCodeAnalyzerParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamSimple" ):
                return visitor.visitParamSimple(self)
            else:
                return visitor.visitChildren(self)


    class ParamObjectContext(ParameterContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PseudoCodeAnalyzerParser.ParameterContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CLASS(self):
            return self.getToken(PseudoCodeAnalyzerParser.CLASS, 0)
        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PseudoCodeAnalyzerParser.ID)
            else:
                return self.getToken(PseudoCodeAnalyzerParser.ID, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamObject" ):
                return visitor.visitParamObject(self)
            else:
                return visitor.visitChildren(self)



    def parameter(self):

        localctx = PseudoCodeAnalyzerParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = PseudoCodeAnalyzerParser.ParamObjectContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.match(PseudoCodeAnalyzerParser.CLASS)
                self.state = 97
                self.match(PseudoCodeAnalyzerParser.ID)
                self.state = 98
                self.match(PseudoCodeAnalyzerParser.ID)
                pass

            elif la_ == 2:
                localctx = PseudoCodeAnalyzerParser.ParamArrayContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.match(PseudoCodeAnalyzerParser.ID)
                self.state = 100
                self.match(PseudoCodeAnalyzerParser.LBRACKET)
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==47:
                    self.state = 101
                    self.match(PseudoCodeAnalyzerParser.RANGE)


                self.state = 104
                self.match(PseudoCodeAnalyzerParser.RBRACKET)
                pass

            elif la_ == 3:
                localctx = PseudoCodeAnalyzerParser.ParamSimpleContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 105
                self.match(PseudoCodeAnalyzerParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PseudoCodeAnalyzerParser.ID)
            else:
                return self.getToken(PseudoCodeAnalyzerParser.ID, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(PseudoCodeAnalyzerParser.COLON)
            else:
                return self.getToken(PseudoCodeAnalyzerParser.COLON, i)

        def getRuleIndex(self):
            return PseudoCodeAnalyzerParser.RULE_local_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocal_var_decl" ):
                return visitor.visitLocal_var_decl(self)
            else:
                return visitor.visitChildren(self)




    def local_var_decl(self):

        localctx = PseudoCodeAnalyzerParser.Local_var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_local_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(PseudoCodeAnalyzerParser.ID)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 109
                self.match(PseudoCodeAnalyzerParser.COLON)
                self.state = 110
                self.match(PseudoCodeAnalyzerParser.ID)
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_list" ):
                return visitor.visitStatement_list(self)
            else:
                return visitor.visitChildren(self)




    def statement_list(self):

        localctx = PseudoCodeAnalyzerParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_statement_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 281474977115392) != 0):
                self.state = 116
                self.statement()
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 117
                    self.match(PseudoCodeAnalyzerParser.T__2)


                self.state = 124
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


        def return_statement(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.Return_statementContext,0)


        def getRuleIndex(self):
            return PseudoCodeAnalyzerParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = PseudoCodeAnalyzerParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statement)
        try:
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48]:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.assignment()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.for_loop()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 127
                self.while_loop()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 128
                self.repeat_loop()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 5)
                self.state = 129
                self.if_statement()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 6)
                self.state = 130
                self.call_statement()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 7)
                self.state = 131
                self.return_statement()
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

        def target_var(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.Target_varContext,0)


        def ASSIGN(self):
            return self.getToken(PseudoCodeAnalyzerParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PseudoCodeAnalyzerParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = PseudoCodeAnalyzerParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.target_var()
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


    class Target_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PseudoCodeAnalyzerParser.RULE_target_var

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VarArrayContext(Target_varContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PseudoCodeAnalyzerParser.Target_varContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(PseudoCodeAnalyzerParser.ID, 0)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarArray" ):
                return visitor.visitVarArray(self)
            else:
                return visitor.visitChildren(self)


    class VarFieldContext(Target_varContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PseudoCodeAnalyzerParser.Target_varContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PseudoCodeAnalyzerParser.ID)
            else:
                return self.getToken(PseudoCodeAnalyzerParser.ID, i)
        def DOT(self):
            return self.getToken(PseudoCodeAnalyzerParser.DOT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarField" ):
                return visitor.visitVarField(self)
            else:
                return visitor.visitChildren(self)


    class VarSimpleContext(Target_varContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PseudoCodeAnalyzerParser.Target_varContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(PseudoCodeAnalyzerParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarSimple" ):
                return visitor.visitVarSimple(self)
            else:
                return visitor.visitChildren(self)



    def target_var(self):

        localctx = PseudoCodeAnalyzerParser.Target_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_target_var)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = PseudoCodeAnalyzerParser.VarArrayContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.match(PseudoCodeAnalyzerParser.ID)
                self.state = 143 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 139
                        self.match(PseudoCodeAnalyzerParser.LBRACKET)
                        self.state = 140
                        self.expression(0)
                        self.state = 141
                        self.match(PseudoCodeAnalyzerParser.RBRACKET)

                    else:
                        raise NoViableAltException(self)
                    self.state = 145 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                pass

            elif la_ == 2:
                localctx = PseudoCodeAnalyzerParser.VarFieldContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.match(PseudoCodeAnalyzerParser.ID)
                self.state = 148
                self.match(PseudoCodeAnalyzerParser.DOT)
                self.state = 149
                self.match(PseudoCodeAnalyzerParser.ID)
                pass

            elif la_ == 3:
                localctx = PseudoCodeAnalyzerParser.VarSimpleContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop" ):
                return visitor.visitFor_loop(self)
            else:
                return visitor.visitChildren(self)




    def for_loop(self):

        localctx = PseudoCodeAnalyzerParser.For_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_for_loop)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_loop" ):
                return visitor.visitWhile_loop(self)
            else:
                return visitor.visitChildren(self)




    def while_loop(self):

        localctx = PseudoCodeAnalyzerParser.While_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_while_loop)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepeat_loop" ):
                return visitor.visitRepeat_loop(self)
            else:
                return visitor.visitChildren(self)




    def repeat_loop(self):

        localctx = PseudoCodeAnalyzerParser.Repeat_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_repeat_loop)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = PseudoCodeAnalyzerParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_if_statement)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = PseudoCodeAnalyzerParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_call_statement)
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 850747457536128) != 0):
                self.state = 198
                self.expression(0)
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==41:
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


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(PseudoCodeAnalyzerParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PseudoCodeAnalyzerParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = PseudoCodeAnalyzerParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(PseudoCodeAnalyzerParser.RETURN)
            self.state = 211
            self.expression(0)
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


        def getRuleIndex(self):
            return PseudoCodeAnalyzerParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExprAddSubContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PseudoCodeAnalyzerParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudoCodeAnalyzerParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PseudoCodeAnalyzerParser.ExpressionContext,i)

        def OP_ADD(self):
            return self.getToken(PseudoCodeAnalyzerParser.OP_ADD, 0)
        def OP_SUB(self):
            return self.getToken(PseudoCodeAnalyzerParser.OP_SUB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAddSub" ):
                return visitor.visitExprAddSub(self)
            else:
                return visitor.visitChildren(self)


    class ExprAndContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PseudoCodeAnalyzerParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudoCodeAnalyzerParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PseudoCodeAnalyzerParser.ExpressionContext,i)

        def OP_AND(self):
            return self.getToken(PseudoCodeAnalyzerParser.OP_AND, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAnd" ):
                return visitor.visitExprAnd(self)
            else:
                return visitor.visitChildren(self)


    class ExprParenContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PseudoCodeAnalyzerParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(PseudoCodeAnalyzerParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(PseudoCodeAnalyzerParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprParen" ):
                return visitor.visitExprParen(self)
            else:
                return visitor.visitChildren(self)


    class ExprMulDivContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PseudoCodeAnalyzerParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudoCodeAnalyzerParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PseudoCodeAnalyzerParser.ExpressionContext,i)

        def OP_MUL(self):
            return self.getToken(PseudoCodeAnalyzerParser.OP_MUL, 0)
        def OP_DIV_REAL(self):
            return self.getToken(PseudoCodeAnalyzerParser.OP_DIV_REAL, 0)
        def OP_MOD(self):
            return self.getToken(PseudoCodeAnalyzerParser.OP_MOD, 0)
        def OP_DIV_INT(self):
            return self.getToken(PseudoCodeAnalyzerParser.OP_DIV_INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprMulDiv" ):
                return visitor.visitExprMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class ExprOrContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PseudoCodeAnalyzerParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudoCodeAnalyzerParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PseudoCodeAnalyzerParser.ExpressionContext,i)

        def OP_OR(self):
            return self.getToken(PseudoCodeAnalyzerParser.OP_OR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprOr" ):
                return visitor.visitExprOr(self)
            else:
                return visitor.visitChildren(self)


    class ExprAtomContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PseudoCodeAnalyzerParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.AtomContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAtom" ):
                return visitor.visitExprAtom(self)
            else:
                return visitor.visitChildren(self)


    class ExprCeilContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PseudoCodeAnalyzerParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CEIL(self):
            return self.getToken(PseudoCodeAnalyzerParser.CEIL, 0)
        def expression(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.ExpressionContext,0)

        def CEIL_CLOSE(self):
            return self.getToken(PseudoCodeAnalyzerParser.CEIL_CLOSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprCeil" ):
                return visitor.visitExprCeil(self)
            else:
                return visitor.visitChildren(self)


    class ExprFloorContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PseudoCodeAnalyzerParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOOR(self):
            return self.getToken(PseudoCodeAnalyzerParser.FLOOR, 0)
        def expression(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.ExpressionContext,0)

        def FLOOR_CLOSE(self):
            return self.getToken(PseudoCodeAnalyzerParser.FLOOR_CLOSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprFloor" ):
                return visitor.visitExprFloor(self)
            else:
                return visitor.visitChildren(self)


    class ExprNotContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PseudoCodeAnalyzerParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OP_NOT(self):
            return self.getToken(PseudoCodeAnalyzerParser.OP_NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprNot" ):
                return visitor.visitExprNot(self)
            else:
                return visitor.visitChildren(self)


    class ExprRelationalContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PseudoCodeAnalyzerParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudoCodeAnalyzerParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PseudoCodeAnalyzerParser.ExpressionContext,i)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprRelational" ):
                return visitor.visitExprRelational(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PseudoCodeAnalyzerParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                localctx = PseudoCodeAnalyzerParser.ExprParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 214
                self.match(PseudoCodeAnalyzerParser.LPAREN)
                self.state = 215
                self.expression(0)
                self.state = 216
                self.match(PseudoCodeAnalyzerParser.RPAREN)
                pass
            elif token in [26]:
                localctx = PseudoCodeAnalyzerParser.ExprCeilContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 218
                self.match(PseudoCodeAnalyzerParser.CEIL)
                self.state = 219
                self.expression(0)
                self.state = 220
                self.match(PseudoCodeAnalyzerParser.CEIL_CLOSE)
                pass
            elif token in [28]:
                localctx = PseudoCodeAnalyzerParser.ExprFloorContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 222
                self.match(PseudoCodeAnalyzerParser.FLOOR)
                self.state = 223
                self.expression(0)
                self.state = 224
                self.match(PseudoCodeAnalyzerParser.FLOOR_CLOSE)
                pass
            elif token in [38]:
                localctx = PseudoCodeAnalyzerParser.ExprNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 226
                self.match(PseudoCodeAnalyzerParser.OP_NOT)
                self.state = 227
                self.expression(7)
                pass
            elif token in [7, 39, 40, 48, 49]:
                localctx = PseudoCodeAnalyzerParser.ExprAtomContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 228
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 248
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 246
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = PseudoCodeAnalyzerParser.ExprMulDivContext(self, PseudoCodeAnalyzerParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 231
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 232
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 62914560) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 233
                        self.expression(7)
                        pass

                    elif la_ == 2:
                        localctx = PseudoCodeAnalyzerParser.ExprAddSubContext(self, PseudoCodeAnalyzerParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 234
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 235
                        _la = self._input.LA(1)
                        if not(_la==20 or _la==21):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 236
                        self.expression(6)
                        pass

                    elif la_ == 3:
                        localctx = PseudoCodeAnalyzerParser.ExprRelationalContext(self, PseudoCodeAnalyzerParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 237
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 238
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 67645734912) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 239
                        self.expression(5)
                        pass

                    elif la_ == 4:
                        localctx = PseudoCodeAnalyzerParser.ExprAndContext(self, PseudoCodeAnalyzerParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 240
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 241
                        self.match(PseudoCodeAnalyzerParser.OP_AND)
                        self.state = 242
                        self.expression(4)
                        pass

                    elif la_ == 5:
                        localctx = PseudoCodeAnalyzerParser.ExprOrContext(self, PseudoCodeAnalyzerParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 243
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 244
                        self.match(PseudoCodeAnalyzerParser.OP_OR)
                        self.state = 245
                        self.expression(3)
                        pass

             
                self.state = 250
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(PseudoCodeAnalyzerParser.NUMBER, 0)

        def TRUE(self):
            return self.getToken(PseudoCodeAnalyzerParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(PseudoCodeAnalyzerParser.FALSE, 0)

        def NULL(self):
            return self.getToken(PseudoCodeAnalyzerParser.NULL, 0)

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

        def target_var(self):
            return self.getTypedRuleContext(PseudoCodeAnalyzerParser.Target_varContext,0)


        def getRuleIndex(self):
            return PseudoCodeAnalyzerParser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = PseudoCodeAnalyzerParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.match(PseudoCodeAnalyzerParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self.match(PseudoCodeAnalyzerParser.TRUE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 253
                self.match(PseudoCodeAnalyzerParser.FALSE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 254
                self.match(PseudoCodeAnalyzerParser.NULL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 255
                self.match(PseudoCodeAnalyzerParser.ID)
                self.state = 256
                self.match(PseudoCodeAnalyzerParser.LPAREN)
                self.state = 265
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 850747457536128) != 0):
                    self.state = 257
                    self.expression(0)
                    self.state = 262
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==41:
                        self.state = 258
                        self.match(PseudoCodeAnalyzerParser.COLON)
                        self.state = 259
                        self.expression(0)
                        self.state = 264
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 267
                self.match(PseudoCodeAnalyzerParser.RPAREN)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 268
                self.target_var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[18] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




