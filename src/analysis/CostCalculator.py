# src/analysis/CostCalculator.py

from ..parsing.PseudoCodeAnalyzerVisitor import PseudoCodeAnalyzerVisitor
from ..parsing.PseudoCodeAnalyzerParser import PseudoCodeAnalyzerParser
from ..llm_integration.LLM_Client import LLMClient

class AnalysisResult:
    def __init__(self, worst_case=None, line_analysis=None):
        self.worst_case = worst_case
        self.line_analysis = line_analysis if line_analysis else []

class CostCalculator(PseudoCodeAnalyzerVisitor):
    def __init__(self, llm_client):
        self.llm_client = llm_client 
        self.current_algorithm_name = None 
        self.is_recursive = False
        self.line_logs = [] # Lista para guardar el análisis línea por línea

    # Método auxiliar para registrar el costo de una línea específica
    def _log_step(self, ctx, cost):
        if ctx and hasattr(ctx, 'start'):
            line_num = ctx.start.line
            self.line_logs.append({
                "line": line_num,
                "cost": str(cost)
            })

    # -------------------------------------------------------------
    # MÉTODO RAÍZ (PROGRAM)
    # -------------------------------------------------------------
    def visitProgram(self, ctx:PseudoCodeAnalyzerParser.ProgramContext):
        final_cost = "0"
        # Analizamos la primera subrutina encontrada
        if ctx.subroutine_declaration(0):
            final_cost = self.visit(ctx.subroutine_declaration(0)).worst_case
        
        return AnalysisResult(worst_case=final_cost, line_analysis=self.line_logs)

    # -------------------------------------------------------------
    # MÉTODO PRINCIPAL (SUBRUTINA)
    # -------------------------------------------------------------
    def visitSubroutine_declaration(self, ctx:PseudoCodeAnalyzerParser.Subroutine_declarationContext):
        self.current_algorithm_name = ctx.ID().getText()
        self.is_recursive = False
        print(f"  > Analizando subrutina: {self.current_algorithm_name}")
        
        body_cost_str = "0"
        if ctx.statement_list(): 
            body_cost_str = self.visit(ctx.statement_list())
        
        final_cost_description = ""
        
        if self.is_recursive:
            # Si es recursivo, enviamos la ecuación completa T(n) = ...
            # El LLM decidirá si usa Teorema Maestro, Árbol o Iteración
            recurrence_relation = f"T(n) = {body_cost_str}"
            print(f"  > Relación de Recurrencia detectada: {recurrence_relation}")
            print("  > Solicitando resolución de recurrencia al LLM...")
            
            llm_response = self.llm_client.solve_equation(
                "relación de recurrencia", 
                recurrence_relation
            )
            final_cost_description = llm_response
            
        else:
            # Si es iterativo (Sumatorias)
            print(f"  > Costo Iterativo (T(n)): {body_cost_str}")
            final_cost_description = body_cost_str

        self.current_algorithm_name = None
        print(f"  > Costo T(n) preliminar para {ctx.ID().getText()}: {final_cost_description}")
        
        return AnalysisResult(worst_case=final_cost_description)

    # -------------------------------------------------------------
    # LISTA DE SENTENCIAS (Suma de costos)
    # -------------------------------------------------------------
    def visitStatement_list(self, ctx:PseudoCodeAnalyzerParser.Statement_listContext):
        total_cost = []
        for statement_ctx in ctx.statement():
            # Visitamos cada sentencia
            costo_sentencia = self.visit(statement_ctx)
            # Si por alguna razón devuelve None (error), lo tratamos como "0"
            if costo_sentencia is None:
                costo_sentencia = "0"
            total_cost.append(str(costo_sentencia))
            
        if not total_cost:
            return "0"
        
        return " + ".join(total_cost)

    # -------------------------------------------------------------
    # ASIGNACIÓN (O(1) o Recursiva)
    # -------------------------------------------------------------
    def visitAssignment(self, ctx:PseudoCodeAnalyzerParser.AssignmentContext):
        cost_of_expression = self.visit(ctx.expression())
        
        final_cost = "1"
        # Si la expresión tiene T(...) es recursiva, propagamos ese costo
        if "T(" in str(cost_of_expression):
             final_cost = cost_of_expression
        elif str(cost_of_expression).isdigit():
             final_cost = "1"
        else:
             final_cost = f"(1 + {cost_of_expression})"
        
        self._log_step(ctx, final_cost)
        return final_cost

    # -------------------------------------------------------------
    # CONTROL DE FLUJO: IF / ELSE
    # -------------------------------------------------------------
    def visitIf_statement(self, ctx:PseudoCodeAnalyzerParser.If_statementContext):
        cost_condition = "1"
        
        # Calculamos costo del bloque THEN
        cost_then = "0"
        if ctx.statement_list(0):
            cost_then = self.visit(ctx.statement_list(0))
            
        # Calculamos costo del bloque ELSE (si existe)
        cost_else = "0"
        if ctx.ELSE():
            cost_else = self.visit(ctx.statement_list(1))
            
        # Construimos la expresión del peor caso: 1 + max(then, else)
        final_cost = f"( {cost_condition} + max({cost_then}, {cost_else}) )"
        
        self._log_step(ctx, final_cost) 
        return final_cost

    # -------------------------------------------------------------
    # CONTROL DE FLUJO: FOR LOOP (Sumatorias)
    # -------------------------------------------------------------
    def visitFor_loop(self, ctx:PseudoCodeAnalyzerParser.For_loopContext):
        start_expr = self.visit(ctx.expression(0))
        end_expr = self.visit(ctx.expression(1))
        
        # Obtenemos el costo del cuerpo del ciclo
        cost_body = "0"
        if ctx.statement_list():
            cost_body = self.visit(ctx.statement_list())
            
        loop_var = ctx.ID().getText()
        
        # Creamos el prompt para el LLM
        summation_expression = (
            f"Por favor, resuelve la siguiente sumatoria y dame la complejidad asintótica (Theta, O, o Omega) "
            f"simplificada.\n\n"
            f"Sumatoria desde {loop_var} = {start_expr} hasta {end_expr} de [ {cost_body} ]\n\n"
            f"Considera 'n' como la variable de tamaño de entrada principal. "
            f"Otras variables (como 'i', si aparecen en los límites o el cuerpo) "
            f"deben ser tratadas como variables de un ciclo externo."
        )

        print(f"  > Solicitando resolución de sumatoria al LLM (Límites: {loop_var}={start_expr} a {end_expr})...")
        llm_response = self.llm_client.solve_equation("sumatoria", summation_expression)
        
        self._log_step(ctx, llm_response)
        return llm_response

    # -------------------------------------------------------------
    # CONTROL DE FLUJO: WHILE LOOP (Aproximación)
    # -------------------------------------------------------------
    def visitWhile_loop(self, ctx:PseudoCodeAnalyzerParser.While_loopContext):
        cost_body = self.visit(ctx.statement_list())
        condition = ctx.expression().getText() # Texto crudo de la condición
        
        # Preguntamos al LLM la complejidad aproximada basándonos en la condición y el cuerpo
        prompt = (
            f"Dada un bucle WHILE con condición '{condition}' y un costo del cuerpo de '{cost_body}', "
            f"¿Cuál es la complejidad asintótica aproximada? Responde solo con la notación (ej. O(log n), O(n))."
        )
        llm_response = self.llm_client.solve_equation("complejidad while", prompt)
        
        self._log_step(ctx, llm_response)
        return llm_response

    # -------------------------------------------------------------
    # LLAMADA A SUBRUTINA (CALL)
    # -------------------------------------------------------------
    def visitCall_statement(self, ctx:PseudoCodeAnalyzerParser.Call_statementContext):
        called_name = ctx.ID().getText()
        
        # Verificar si es una llamada recursiva (se llama a sí mismo)
        if called_name == self.current_algorithm_name:
            print(f"  > ¡Recursión detectada (CALL)!: {called_name}")
            self.is_recursive = True
            
            param_str = "n"
            # Intentamos obtener el parámetro que cambia (ej. mitad)
            if ctx.expression():
                # Tomamos el último parámetro como heurística
                param_str = self.visit(ctx.expression()[-1])
            
            cost = f"T({param_str})"
            self._log_step(ctx, cost)
            return cost
            
        else:
            # Es una llamada externa (ej. print)
            print(f"  > (Llamada a subrutina externa: {called_name})")
            cost = "1"
            self._log_step(ctx, cost)
            return cost

    # -------------------------------------------------------------
    # EXPRESIONES Y VARIABLES
    # -------------------------------------------------------------
    def visitVariable(self, ctx:PseudoCodeAnalyzerParser.VariableContext):
        return ctx.getText()

    def visitExpression(self, ctx:PseudoCodeAnalyzerParser.ExpressionContext):
        # 1. Llamada a función dentro de expresión (ej. x <- FACTORIAL(n-1))
        if ctx.ID() and ctx.LPAREN():
            function_name = ctx.ID().getText()
            
            if function_name == self.current_algorithm_name:
                print(f"  > ¡Recursión detectada (Expr)!: {function_name}")
                self.is_recursive = True
                
                param_str = "n"
                if ctx.expression(0):
                    param_str = self.visit(ctx.expression(0))
                return f"T({param_str})"
            else:
                return "1" # Función externa es O(1)

        # 2. Paréntesis
        if ctx.LPAREN() and len(ctx.expression()) == 1:
            return self.visit(ctx.expression(0))
            
        # 3. Terminales
        if ctx.NUMBER(): return ctx.NUMBER().getText()
        if ctx.variable(): return self.visit(ctx.variable())
                
        # 4. Operaciones Binarias (+, -, *, /)
        if len(ctx.expression()) == 2:
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            
            op = "+" 
            if ctx.OP_MUL(): op = "*"
            elif ctx.OP_DIV_REAL() or ctx.OP_DIV_ENTERA(): op = "/"
            elif ctx.OP_SUB(): op = "-"
            
            # Devolvemos la expresión completa para que el LLM la analice
            return f"({left} {op} {right})"
        
        return ctx.getText()