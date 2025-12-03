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


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#structure_definition.
    def visitStructure_definition(self, ctx:PseudoCodeAnalyzerParser.Structure_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#class_definition.
    def visitClass_definition(self, ctx:PseudoCodeAnalyzerParser.Class_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#array_definition.
    def visitArray_definition(self, ctx:PseudoCodeAnalyzerParser.Array_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#algorithm_definition.
    def visitAlgorithm_definition(self, ctx:PseudoCodeAnalyzerParser.Algorithm_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#param_list.
    def visitParam_list(self, ctx:PseudoCodeAnalyzerParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#ParamObject.
    def visitParamObject(self, ctx:PseudoCodeAnalyzerParser.ParamObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#ParamArray.
    def visitParamArray(self, ctx:PseudoCodeAnalyzerParser.ParamArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#ParamSimple.
    def visitParamSimple(self, ctx:PseudoCodeAnalyzerParser.ParamSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#local_var_decl.
    def visitLocal_var_decl(self, ctx:PseudoCodeAnalyzerParser.Local_var_declContext):
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


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#VarArray.
    def visitVarArray(self, ctx:PseudoCodeAnalyzerParser.VarArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#VarField.
    def visitVarField(self, ctx:PseudoCodeAnalyzerParser.VarFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#VarSimple.
    def visitVarSimple(self, ctx:PseudoCodeAnalyzerParser.VarSimpleContext):
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


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#return_statement.
    def visitReturn_statement(self, ctx:PseudoCodeAnalyzerParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#ExprAddSub.
    def visitExprAddSub(self, ctx:PseudoCodeAnalyzerParser.ExprAddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#ExprAnd.
    def visitExprAnd(self, ctx:PseudoCodeAnalyzerParser.ExprAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#ExprParen.
    def visitExprParen(self, ctx:PseudoCodeAnalyzerParser.ExprParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#ExprMulDiv.
    def visitExprMulDiv(self, ctx:PseudoCodeAnalyzerParser.ExprMulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#ExprOr.
    def visitExprOr(self, ctx:PseudoCodeAnalyzerParser.ExprOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#ExprAtom.
    def visitExprAtom(self, ctx:PseudoCodeAnalyzerParser.ExprAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#ExprCeil.
    def visitExprCeil(self, ctx:PseudoCodeAnalyzerParser.ExprCeilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#ExprFloor.
    def visitExprFloor(self, ctx:PseudoCodeAnalyzerParser.ExprFloorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#ExprNot.
    def visitExprNot(self, ctx:PseudoCodeAnalyzerParser.ExprNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#ExprRelational.
    def visitExprRelational(self, ctx:PseudoCodeAnalyzerParser.ExprRelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoCodeAnalyzerParser#atom.
    def visitAtom(self, ctx:PseudoCodeAnalyzerParser.AtomContext):
        return self.visitChildren(ctx)



del PseudoCodeAnalyzerParser