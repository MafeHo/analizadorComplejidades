# Generated from src/parsing/PseudoCodeAnalyzer.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PseudoCodeAnalyzerParser import PseudoCodeAnalyzerParser
else:
    from PseudoCodeAnalyzerParser import PseudoCodeAnalyzerParser

# This class defines a complete generic visitor for a parse tree produced by PseudoCodeAnalyzerParser.

class PseudoCodeAnalyzerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PseudoCodeAnalyzerParser#program.
    def visitProgram(self, ctx:PseudoCodeAnalyzerParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#class_declaration.
    def visitClass_declaration(self, ctx:PseudoCodeAnalyzerParser.Class_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#local_vars_declaration.
    def visitLocal_vars_declaration(self, ctx:PseudoCodeAnalyzerParser.Local_vars_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#subroutine_declaration.
    def visitSubroutine_declaration(self, ctx:PseudoCodeAnalyzerParser.Subroutine_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#parameter_declaration.
    def visitParameter_declaration(self, ctx:PseudoCodeAnalyzerParser.Parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#statement_list.
    def visitStatement_list(self, ctx:PseudoCodeAnalyzerParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#statement.
    def visitStatement(self, ctx:PseudoCodeAnalyzerParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#assignment.
    def visitAssignment(self, ctx:PseudoCodeAnalyzerParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#variable.
    def visitVariable(self, ctx:PseudoCodeAnalyzerParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#for_loop.
    def visitFor_loop(self, ctx:PseudoCodeAnalyzerParser.For_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#while_loop.
    def visitWhile_loop(self, ctx:PseudoCodeAnalyzerParser.While_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#repeat_loop.
    def visitRepeat_loop(self, ctx:PseudoCodeAnalyzerParser.Repeat_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#if_statement.
    def visitIf_statement(self, ctx:PseudoCodeAnalyzerParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#call_statement.
    def visitCall_statement(self, ctx:PseudoCodeAnalyzerParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#expression.
    def visitExpression(self, ctx:PseudoCodeAnalyzerParser.ExpressionContext):
        return self.visitChildren(ctx)



del PseudoCodeAnalyzerParser