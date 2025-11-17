# src/analysis/CostCalculator.py (Versión con RECURSIÓN CORREGIDA FINAL)

from ..parsing.PseudoCodeAnalyzerVisitor import PseudoCodeAnalyzerVisitor
from ..parsing.PseudoCodeAnalyzerParser import PseudoCodeAnalyzerParser
from ..llm_integration.LLM_Client import LLMClient

# (Clase AnalysisResult se mantiene igual)
class AnalysisResult:
    def __init__(self, worst_case=None, best_case=None, avg_case=None, line_analysis=None, reasoning=""):
        self.worst_case = worst_case
        self.best_case = best_case
        self.avg_case = avg_case
        self.reasoning = reasoning
        self.line_analysis = line_analysis if line_analysis else []

class CostCalculator(PseudoCodeAnalyzerVisitor):
    def __init__(self, llm_client):
        self.llm_client = llm_client 
        self.cost_map = {}
        self.current_algorithm_name = None 
        self.is_recursive = False
        self.line_logs = []

    def _log_step(self, ctx, cost):
        line_num = ctx.start.line
        # Obtenemos el texto original de la línea (limpiando espacios)
        text = ctx.getText() # Esto puede ser sucio, mejor tomamos solo un ID visual
        # Nota: ANTLR a veces junta todo el texto. Para el reporte, usaremos el número de línea.
        self.line_logs.append({
            "line": line_num,
            "cost": str(cost)
        })

    # -------------------------------------------------------------
    # MÉTODO RAÍZ (PROGRAM)
    # -------------------------------------------------------------
    def visitProgram(self, ctx:PseudoCodeAnalyzerParser.ProgramContext):
        final_cost = "0"
        if ctx.subroutine_declaration(0):
            #return self.visit(ctx.subroutine_declaration(0))
            final_cost = self.visit(ctx.subroutine_declaration(0)).worst_case
        return AnalysisResult(worst_case=final_cost, line_analysis=self.line_logs)
       # return AnalysisResult(worst_case="ERROR: No se encontró subrutina")

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
            
        #else:
         #   print(f"  > ERROR: No se pudo parsear el cuerpo de '{self.current_algorithm_name}'.")
          #  body_cost_str = "ERROR_PARSING"

        final_cost_description = ""
        
        """if self.is_recursive:
            # Si se detectó recursión, el 'body_cost_str' es la
            # función de costo del IF/ELSE, ej: ( 1 + max(1, T((n - 1))) )
            
            # Simplificamos para el LLM: T(n) = T(n-k) + f(n)
            recursive_term = ""
            if "T(" in body_cost_str:
                start = body_cost_str.find("T(")
                end = body_cost_str.find(")", start) + 1
                recursive_term = body_cost_str[start:end] # ej. T((n - 1))
            
            # El costo del trabajo 'f(n)' es el resto (simplificado a '1' (O(1)))
            fn_cost = "1" 

            recurrence_relation = f"T(n) = {recursive_term} + {fn_cost}"""
        
        if self.is_recursive:
            # body_cost_str ahora es la expresión de costo completa del 
            # if/else, ej: "( 1 + max(1, T((n - 1))) )"
            
            # --- INICIO DE LA CORRECCIÓN ---
            # No simplificamos manualmente. Enviamos la expresión completa
            # que el visitador ya calculó. El LLM interpretará 
            # la recurrencia y el costo constante f(n) desde aquí.
            
            recurrence_relation = f"T(n) = {body_cost_str}"
            # --- FIN DE LA CORRECCIÓN ---
            
            print(f"  > Relación de Recurrencia detectada: {recurrence_relation}")
            print("  > Solicitando resolución de recurrencia al LLM...")
            
            llm_response = self.llm_client.solve_equation(
                "relación de recurrencia", 
                recurrence_relation
            )
            final_cost_description = llm_response
            
        else:
            # Si NO es recursivo
            print(f"  > Costo Iterativo (T(n)): {body_cost_str}")
            final_cost_description = body_cost_str

        self.current_algorithm_name = None
        
        print(f"  > Costo T(n) preliminar para {ctx.ID().getText()}: {final_cost_description}")
        return AnalysisResult(worst_case=final_cost_description)

    # -------------------------------------------------------------
    # Manejo de Bloques de Sentencias (Suma de Costos)
    # -------------------------------------------------------------
    def visitStatement_list(self, ctx:PseudoCodeAnalyzerParser.Statement_listContext):
        total_cost = []
        for statement_ctx in ctx.statement():
            costo_sentencia = self.visit(statement_ctx)
            total_cost.append(str(costo_sentencia))
            
        if not total_cost:
            return 0
        
        return " + ".join(total_cost)

    # -------------------------------------------------------------
    # Sentencias O(1)
    # -------------------------------------------------------------
    def visitAssignment(self, ctx:PseudoCodeAnalyzerParser.AssignmentContext):
        # El costo de la asignación es 1 (para la asignación en sí)
        # MÁS el costo de la expresión que se está asignando.
        cost_of_expression = self.visit(ctx.expression())
        
        # Si la expresión es recursiva (ej. T(n-1)), solo propagamos ese costo.
        if "T(" in str(cost_of_expression):
             return cost_of_expression
             
        # Si la expresión es un número (ej. 1), el costo es 1 (asignación) + 0 (evaluación)
        if str(cost_of_expression).isdigit():
             return 1
             
        # Si es una expresión aritmética (ej. n * 2), el costo es 1 + costo(expresión)
        return f"(1 + {cost_of_expression})"
    


    # -------------------------------------------------------------
    # Control de Flujo (IF/ELSE)
    # -------------------------------------------------------------
    def visitIf_statement(self, ctx:PseudoCodeAnalyzerParser.If_statementContext):
        cost_condition = "1"
        cost_then = self.visit(ctx.statement_list(0))
        cost_else = "0"
        if ctx.ELSE():
            cost_else = self.visit(ctx.statement_list(1))
            
        # Devolvemos el peor caso
        return f"( {cost_condition} + max({cost_then}, {cost_else}) )"


    # src/analysis/CostCalculator.py

    # -------------------------------------------------------------
    # Control de Flujo (FOR Loop)
    # -------------------------------------------------------------
    def visitFor_loop(self, ctx:PseudoCodeAnalyzerParser.For_loopContext):
        start_expr = self.visit(ctx.expression(0)) # ej. 1
        end_expr = self.visit(ctx.expression(1))   # ej. (n - 1) o (n - i)
        cost_body = self.visit(ctx.statement_list()) # ej. O(1) o Theta(n-i)

        loop_var = ctx.ID().getText() # ej. i o j

        # --- INICIO DE LA CORRECCIÓN ---
        # El prompt ahora es consciente del contexto.
        # Informamos al LLM sobre la variable de entrada 'n' y
        # le pedimos que resuelva la sumatoria tal como está.

        summation_expression = (
        f"Por favor, resuelve la siguiente sumatoria y dame la complejidad asintótica (Theta, O, o Omega) "
        f"simplificada.\n\n"
        f"Sumatoria desde {loop_var} = {start_expr} hasta {end_expr} de [ {cost_body} ]\n\n"
        f"Considera 'n' como la variable de tamaño de entrada principal. "
        f"Otras variables (como 'i', si aparecen en los límites o el cuerpo) "
        f"deben ser tratadas como variables de un ciclo externo."
        )

        print(f"> Solicitando resolución de sumatoria al LLM (Límites: {loop_var}={start_expr} a {end_expr})...")
        llm_response = self.llm_client.solve_equation("sumatoria", summation_expression)

        #pa la tabla con los costos por línea
        self._log_step(ctx, llm_response)

        # Con la nueva instrucción de sistema, llm_response será una cadena limpia
        #section: # (ej. "Theta(n^2)") y no contaminará prompts futuros
        return llm_response
        # --- FIN DE LA CORRECCIÓN ---

    # -------------------------------------------------------------
    # LLAMADA A SUBRUTINA (Statement)
    # -------------------------------------------------------------
    def visitCall_statement(self, ctx:PseudoCodeAnalyzerParser.Call_statementContext):
        called_name = ctx.ID().getText()
        print(f"  > (Llamada a subrutina externa: {called_name})")
        return self.cost_map.get(called_name, "1") # Asumir O(1)

    
    # -------------------------------------------------------------
    # MÉTODOS DE EXPRESIÓN (¡LÓGICA DE RECURSIÓN CORREGIDA!)
    # -------------------------------------------------------------

    # -------------------------------------------------------------
    # MÉTODOS DE EXPRESIÓN (¡CORREGIDO PARA MÚLTIPLES RECURSIONES!)
    # -------------------------------------------------------------

    def visitVariable(self, ctx:PseudoCodeAnalyzerParser.VariableContext):
        return ctx.getText()

    def visitExpression(self, ctx:PseudoCodeAnalyzerParser.ExpressionContext):
        
        # --- 1. LÓGICA DE RECURSIÓN (Función) ---
        # Es una llamada ID(expression), ej: FACTORIAL(n-1)
        if ctx.ID() and ctx.LPAREN():
            function_name = ctx.ID().getText()
            
            if function_name == self.current_algorithm_name:
                # ¡RECURSIÓN DETECTADA!
                print(f"  > ¡Recursión detectada!: {function_name}")
                self.is_recursive = True
                
                param_str = "n"
                if ctx.expression(0):
                    param_str = self.visit(ctx.expression(0)) # ej. (n - 1)
                
                # Devolver el T(n) simbólico
                return f"T({param_str})"
            else:
                # Es una llamada a función externa (ej. length(A))
                return "1" # Asumir O(1)

        # --- 2. Paréntesis (expr) ---
        if ctx.LPAREN() and len(ctx.expression()) == 1:
            return self.visit(ctx.expression(0))
            
        # --- 3. Terminales (NUMBER, variable) ---
        if ctx.NUMBER():
            return ctx.NUMBER().getText()
        if ctx.variable():
            return self.visit(ctx.variable())
                
        # --- 4. Operaciones Aritméticas (Suma, Resta, Mul, etc.) ---
        if len(ctx.expression()) == 2:
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            
            # Determinamos el operador
            op = "+" # default
            if ctx.OP_MUL(): op = "*"
            elif ctx.OP_DIV_REAL() or ctx.OP_DIV_ENTERA(): op = "/"
            elif ctx.OP_SUB(): op = "-"
            elif ctx.OP_MOD(): op = "%"
            # Si es ADD o cualquier otro, se queda como "+"

            # --- CORRECCIÓN ---
            # Antes descartábamos 'right' si 'left' tenía T(). 
            # Ahora construimos la cadena completa para que el LLM vea todo.
            # ej: "T(n-1) + 1 + T(n-1)"
            
            return f"({left} {op} {right})"
        
        # --- 5. Fallback ---
        return ctx.getText()
        
        