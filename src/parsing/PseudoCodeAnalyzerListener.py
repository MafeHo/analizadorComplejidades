# Generated from src/parsing/PseudoCodeAnalyzer.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PseudoCodeAnalyzerParser import PseudoCodeAnalyzerParser
else:
    from PseudoCodeAnalyzerParser import PseudoCodeAnalyzerParser

# This class defines a complete listener for a parse tree produced by PseudoCodeAnalyzerParser.
class PseudoCodeAnalyzerListener(ParseTreeListener):

    # Enter a parse tree produced by PseudoCodeAnalyzerParser#program.
    def enterProgram(self, ctx:PseudoCodeAnalyzerParser.ProgramContext):
        pass

    # Exit a parse tree produced by PseudoCodeAnalyzerParser#program.
    def exitProgram(self, ctx:PseudoCodeAnalyzerParser.ProgramContext):
        pass


    # Enter a parse tree produced by PseudoCodeAnalyzerParser#class_declaration.
    def enterClass_declaration(self, ctx:PseudoCodeAnalyzerParser.Class_declarationContext):
        pass

    # Exit a parse tree produced by PseudoCodeAnalyzerParser#class_declaration.
    def exitClass_declaration(self, ctx:PseudoCodeAnalyzerParser.Class_declarationContext):
        pass


    # Enter a parse tree produced by PseudoCodeAnalyzerParser#local_vars_declaration.
    def enterLocal_vars_declaration(self, ctx:PseudoCodeAnalyzerParser.Local_vars_declarationContext):
        pass

    # Exit a parse tree produced by PseudoCodeAnalyzerParser#local_vars_declaration.
    def exitLocal_vars_declaration(self, ctx:PseudoCodeAnalyzerParser.Local_vars_declarationContext):
        pass


    # Enter a parse tree produced by PseudoCodeAnalyzerParser#subroutine_declaration.
    def enterSubroutine_declaration(self, ctx:PseudoCodeAnalyzerParser.Subroutine_declarationContext):
        pass

    # Exit a parse tree produced by PseudoCodeAnalyzerParser#subroutine_declaration.
    def exitSubroutine_declaration(self, ctx:PseudoCodeAnalyzerParser.Subroutine_declarationContext):
        pass


    # Enter a parse tree produced by PseudoCodeAnalyzerParser#parameter_declaration.
    def enterParameter_declaration(self, ctx:PseudoCodeAnalyzerParser.Parameter_declarationContext):
        pass

    # Exit a parse tree produced by PseudoCodeAnalyzerParser#parameter_declaration.
    def exitParameter_declaration(self, ctx:PseudoCodeAnalyzerParser.Parameter_declarationContext):
        pass


    # Enter a parse tree produced by PseudoCodeAnalyzerParser#statement_list.
    def enterStatement_list(self, ctx:PseudoCodeAnalyzerParser.Statement_listContext):
        pass

    # Exit a parse tree produced by PseudoCodeAnalyzerParser#statement_list.
    def exitStatement_list(self, ctx:PseudoCodeAnalyzerParser.Statement_listContext):
        pass


    # Enter a parse tree produced by PseudoCodeAnalyzerParser#statement.
    def enterStatement(self, ctx:PseudoCodeAnalyzerParser.StatementContext):
        pass

    # Exit a parse tree produced by PseudoCodeAnalyzerParser#statement.
    def exitStatement(self, ctx:PseudoCodeAnalyzerParser.StatementContext):
        pass


    # Enter a parse tree produced by PseudoCodeAnalyzerParser#assignment.
    def enterAssignment(self, ctx:PseudoCodeAnalyzerParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PseudoCodeAnalyzerParser#assignment.
    def exitAssignment(self, ctx:PseudoCodeAnalyzerParser.AssignmentContext):
        pass


    # Enter a parse tree produced by PseudoCodeAnalyzerParser#variable.
    def enterVariable(self, ctx:PseudoCodeAnalyzerParser.VariableContext):
        pass

    # Exit a parse tree produced by PseudoCodeAnalyzerParser#variable.
    def exitVariable(self, ctx:PseudoCodeAnalyzerParser.VariableContext):
        pass


    # Enter a parse tree produced by PseudoCodeAnalyzerParser#for_loop.
    def enterFor_loop(self, ctx:PseudoCodeAnalyzerParser.For_loopContext):
        pass

    # Exit a parse tree produced by PseudoCodeAnalyzerParser#for_loop.
    def exitFor_loop(self, ctx:PseudoCodeAnalyzerParser.For_loopContext):
        pass


    # Enter a parse tree produced by PseudoCodeAnalyzerParser#while_loop.
    def enterWhile_loop(self, ctx:PseudoCodeAnalyzerParser.While_loopContext):
        pass

    # Exit a parse tree produced by PseudoCodeAnalyzerParser#while_loop.
    def exitWhile_loop(self, ctx:PseudoCodeAnalyzerParser.While_loopContext):
        pass


    # Enter a parse tree produced by PseudoCodeAnalyzerParser#repeat_loop.
    def enterRepeat_loop(self, ctx:PseudoCodeAnalyzerParser.Repeat_loopContext):
        pass

    # Exit a parse tree produced by PseudoCodeAnalyzerParser#repeat_loop.
    def exitRepeat_loop(self, ctx:PseudoCodeAnalyzerParser.Repeat_loopContext):
        pass


    # Enter a parse tree produced by PseudoCodeAnalyzerParser#if_statement.
    def enterIf_statement(self, ctx:PseudoCodeAnalyzerParser.If_statementContext):
        pass

    # Exit a parse tree produced by PseudoCodeAnalyzerParser#if_statement.
    def exitIf_statement(self, ctx:PseudoCodeAnalyzerParser.If_statementContext):
        pass


    # Enter a parse tree produced by PseudoCodeAnalyzerParser#call_statement.
    def enterCall_statement(self, ctx:PseudoCodeAnalyzerParser.Call_statementContext):
        pass

    # Exit a parse tree produced by PseudoCodeAnalyzerParser#call_statement.
    def exitCall_statement(self, ctx:PseudoCodeAnalyzerParser.Call_statementContext):
        pass


    # Enter a parse tree produced by PseudoCodeAnalyzerParser#expression.
    def enterExpression(self, ctx:PseudoCodeAnalyzerParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PseudoCodeAnalyzerParser#expression.
    def exitExpression(self, ctx:PseudoCodeAnalyzerParser.ExpressionContext):
        pass



del PseudoCodeAnalyzerParser