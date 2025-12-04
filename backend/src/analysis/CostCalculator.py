# src/analysis/CostCalculator.py

from ..parsing.PseudoCodeAnalyzerVisitor import PseudoCodeAnalyzerVisitor
from ..parsing.PseudoCodeAnalyzerParser import PseudoCodeAnalyzerParser
from .MathEngine import MathEngine
from sympy import Integer, Symbol, Max, ceiling, floor

class AnalysisResult:
    def __init__(self, worst_case=None, line_analysis=None, recurrence_eq=None, master_theorem_data=None, explanation=None):
        self.worst_case = worst_case
        self.line_analysis = line_analysis if line_analysis else []
        self.recurrence_eq = recurrence_eq
        self.master_theorem_data = master_theorem_data
        self.explanation = explanation

class CostCalculator(PseudoCodeAnalyzerVisitor):
    def __init__(self):
        self.math = MathEngine()
        self.variables = {} 
        self.current_algorithm_name = None 
        self.is_recursive = False
        self.line_logs = [] 
        self.raw_equation = None 
        self.temp_master_data = None
        self.explanation = None
        self.base_conditions = [] 
        
    def visit(self, tree):
        """Override visit to handle None trees gracefully (e.g. syntax errors)."""
        if tree is None:
            return Integer(0)
        return super().visit(tree)

    def _log_step(self, ctx, cost, details=None):
        if hasattr(ctx, 'start'):
            cost_str = str(cost).replace("**", "^")
            if details:
                # Limpieza visual
                details = str(details).replace("**", "^")
                log_entry = f"OE: {details} -> {cost_str}"
            else:
                log_entry = f"OE: {cost_str} -> {cost_str}"
            self.line_logs.append({"line": ctx.start.line, "cost": log_entry})

    def visitProgram(self, ctx:PseudoCodeAnalyzerParser.ProgramContext):
        algo_ctx = ctx.algorithm_definition()
        complexity_result = self.visit(algo_ctx)
        
        final_str = str(complexity_result)
        if hasattr(self.math, 'format_complexity'):
            raw_str = str(complexity_result).replace("**", "^")
            formatted_str = self.math.format_complexity(complexity_result)
            
            # Asegurar que formatted_str tenga Theta u O
            if "Theta" not in formatted_str and "O(" not in formatted_str:
                formatted_str = f"Theta({formatted_str})"

            # Solo mostrar formatted_str para mantener la estética limpia
            final_str = formatted_str

        return AnalysisResult(
            worst_case=final_str, 
            line_analysis=self.line_logs,
            recurrence_eq=self.raw_equation,
            master_theorem_data=self.temp_master_data,
            explanation=self.explanation
        )

    def visitAlgorithm_definition(self, ctx:PseudoCodeAnalyzerParser.Algorithm_definitionContext):
        self.current_algorithm_name = ctx.ID().getText()
        print(f"Analizando: {self.current_algorithm_name}")
        
        self.variables = {}
        self.is_recursive = False
        self.line_logs = []
        self.raw_equation = None 
        self.temp_master_data = None
        self.explanation = None
        self.base_conditions = [] 
        
        total_cost = Integer(0)
        if ctx.statement_list():
            total_cost = self.visit(ctx.statement_list())
            
        if self.is_recursive:
            # Split cost into recursive and base parts
            rec_cost = self.math.get_recursive_part(total_cost)
            base_cost = self.math.get_base_part(total_cost)
            
            # Format equation
            rec_str = str(rec_cost).replace("**", "^")
            
            # Replace constant terms with O(1) for display
            # Heuristic: if it ends with " + <number>", replace with " + O(1)"
            import re
            rec_str = re.sub(r'\s\+\s\d+$', ' + O(1)', rec_str)
            
            base_str = str(base_cost).replace("**", "^")
            if base_cost.is_number:
                base_str = "O(1)"
            
            cond_str = "Unknown"
            if self.base_conditions:
                # Format base conditions: T(0)=O(1), T(1)=O(1)
                formatted_conditions = []
                for cond in self.base_conditions:
                    # Extract number from condition (e.g. n<=1 -> 1)
                    nums = re.findall(r'\d+', cond)
                    if nums:
                        limit = int(nums[0])
                        # Generate T(0)=O(1), T(1)=O(1) up to limit
                        for i in range(limit + 1):
                             formatted_conditions.append(f"T({i})=O(1)")
                
                if formatted_conditions:
                    base_str = ", ".join(formatted_conditions)
                else:
                    cond_str = " OR ".join(self.base_conditions)
                    base_str = f"Base case: {base_str} (Condition: {cond_str})"
            else:
                 base_str = f"Base case: {base_str}"
            
            eq_str = f"T(n) = {rec_str}, {base_str}"
            print(f"Ecuacion detectada: {eq_str}")
            self.raw_equation = eq_str
            
            # Resolver recurrencia
            solved_data = self.math.solve_recurrence(total_cost)
            
            # Generar explicacion
            self.explanation = self.math.explain_recurrence(solved_data, eq_str)
            
            complexity = solved_data
            if isinstance(solved_data, dict):
                complexity = solved_data.get("complexity")
                self.temp_master_data = solved_data.get("details")
            
            return complexity
        else:
            # Iterative explanation
            self.explanation = self.math.explain_iterative(total_cost)
            return total_cost

    def visitStatement_list(self, ctx:PseudoCodeAnalyzerParser.Statement_listContext):
        cost = Integer(0)
        for stmt in ctx.statement():
            c = self.visit(stmt)
            if c: cost += c
        return cost

    # --- CONTROL DE FLUJO ---
    def visitFor_loop(self, ctx:PseudoCodeAnalyzerParser.For_loopContext):
        var = ctx.ID().getText()
        start = self.visit(ctx.expression(0))
        end = self.visit(ctx.expression(1))
        body_cost = self.visit(ctx.statement_list())
        total = self.math.sum_loop(body_cost, var, start, end)
        
        # OE: Iteraciones * Cuerpo
        iters = (end - start + 1)
        details = f"Sum({var}={start}..{end}) [{iters} iter] * ({body_cost})"
        self._log_step(ctx, total, details=details)
        return total

    def visitWhile_loop(self, ctx:PseudoCodeAnalyzerParser.While_loopContext):
        body_str = ctx.statement_list().getText()
        iters = self.math.n 
        if "*" in body_str or "/" in body_str or "div" in body_str:
            from sympy import log
            iters = log(self.math.n, 2)
        
        header_cost = iters + 1
        body_cost = self.visit(ctx.statement_list())
        total = (body_cost * iters) + header_cost
        
        details = f"{iters} iter * ({body_cost}) + Header"
        self._log_step(ctx, total, details=details)
        return total

    def visitIf_statement(self, ctx:PseudoCodeAnalyzerParser.If_statementContext):
        cond = self._count_ops_in_expr(ctx.expression())
        then_c = self.visit(ctx.statement_list(0))
        else_c = self.visit(ctx.statement_list(1)) if ctx.ELSE() else Integer(0)
        
        # Detect base case condition
        then_has_T = hasattr(then_c, 'has') and then_c.has(self.math.T)
        else_has_T = hasattr(else_c, 'has') and else_c.has(self.math.T)
        
        if self.current_algorithm_name: # Only if inside algorithm
             if not then_has_T:
                 # Potential base case
                 # Check if it looks like a base case check (involves n)
                 if "n" in ctx.expression().getText():
                     self.base_conditions.append(ctx.expression().getText())

        total = cond + Max(then_c, else_c)
        self._log_step(ctx, total, details=f"Max({then_c}, {else_c}) + {cond}")
        return total

    def visitReturn_statement(self, ctx:PseudoCodeAnalyzerParser.Return_statementContext):
        # Visitamos la expresión para ver si hay recursión T(n) dentro
        val = self.visit(ctx.expression())
        
        # Si el valor retornado contiene un costo recursivo T(...), retornamos ese costo
        if hasattr(val, 'has') and val.has(self.math.T):
            # Costo = calcular recursión + 1 retorno
            total = val + 1
            self._log_step(ctx, total, details=f"Return Recursion: {val} + 1")
            return total
            
        # Si es un valor simple (n), el costo es O(1) + operaciones
        cost = self._count_ops_in_expr(ctx.expression()) + 1
        self._log_step(ctx, cost)
        return cost

    def visitAssignment(self, ctx:PseudoCodeAnalyzerParser.AssignmentContext):
        val = self.visit(ctx.expression())
        var = ctx.target_var().getText()
        if "[" not in var: self.variables[var] = val
        
        # Si la expresión contiene una llamada recursiva T(...), el costo es esa recursión + asignación
        if hasattr(val, 'has') and val.has(self.math.T):
            cost = val + 1
            self._log_step(ctx, cost, details=f"Assign Recursion: {val} + 1")
            return cost

        cost = self._count_ops_in_expr(ctx.expression()) + 1
        self._log_step(ctx, cost)
        return cost

    def visitCall_statement(self, ctx:PseudoCodeAnalyzerParser.Call_statementContext):
        func_name = ctx.ID().getText()
        
        # Check for recursion
        if func_name == self.current_algorithm_name:
            self.is_recursive = True
            
            # Get argument
            args = ctx.expression()
            new_size = self.math.n
            
            # Heuristic: Find the argument that looks like a size (contains n or numbers)
            found_size = False
            if args:
                for arg in args:
                    val = self.visit(arg)
                    # Check if val depends on n or is a number
                    if hasattr(val, 'free_symbols') and self.math.n in val.free_symbols:
                        new_size = val
                        found_size = True
                        break
                    if isinstance(val, (int, float)) or (hasattr(val, 'is_number') and val.is_number):
                        # Candidate, but prefer n-dependent
                        new_size = val
                
                # If no n-dependent arg found, fallback to the first one (legacy behavior)
                if not found_size and args:
                     new_size = self.visit(args[0])
            
            cost = self.math.T(new_size)
            self._log_step(ctx, cost, details=f"Recurrencia: T({new_size})")
            return cost
        
        # External call cost
        cost = Integer(1)
        self._log_step(ctx, cost, details="External Call")
        return cost

    # --- VISITORS DE EXPRESIONES ---
    
    def visitExprAtom(self, ctx:PseudoCodeAnalyzerParser.ExprAtomContext):
        # Verificamos si es una llamada a función: ID ( ... )
        atom_ctx = ctx.atom()
        
        # ANTLR guarda tokens hijos. Si hay LPAREN, es llamada o acceso.
        if atom_ctx.LPAREN():
            func_name = atom_ctx.ID().getText()
            
            # DETECCIÓN DE RECURSIÓN EN EXPRESIÓN (Fibonacci + Fibonacci)
            if func_name == self.current_algorithm_name:
                self.is_recursive = True
                
                # Obtener argumento. La gramática es: ID LPAREN (expr (, expr)*)? RPAREN
                # atom context tiene el método expression() que devuelve lista
                args = atom_ctx.expression()
                new_size = self.math.n
                if args:
                    # Visitamos el primer argumento para resolver variables (ej: n-1)
                    new_size = self.visit(args[0])
                
                return self.math.T(new_size)
            
            # Si es otra función, asumimos costo 1 por ahora
            return Integer(1)

        # Si no es función, es variable o número
        txt = atom_ctx.getText()
        if txt.isdigit(): return Integer(int(txt))
        if txt == 'n': return self.math.n
        if txt in self.variables: return self.variables[txt]
        return Symbol(txt.split('[')[0])

    def visitExprParen(self, ctx): return self.visit(ctx.expression())
    
    def visitExprAddSub(self, ctx):
        try:
            e0 = ctx.expression(0)
            e1 = ctx.expression(1)
            if e0 is None or e1 is None:
                return Integer(0)
                
            l = self.visit(e0)
            r = self.visit(e1)
            # Si alguno es un costo recursivo T(...), sumamos los costos
            # Si son valores, operamos aritméticamente
            return l + r if ctx.OP_ADD() else l - r
        except Exception as e:
            print(f"Error in visitExprAddSub: {e}")
            raise e
        
    def visitExprMulDiv(self, ctx):
        l, r = self.visit(ctx.expression(0)), self.visit(ctx.expression(1))
        if ctx.OP_MUL(): return l * r
        if ctx.OP_DIV_REAL(): return l / r
        return floor(l / r)

    def visitExprCeil(self, ctx): return ceiling(self.visit(ctx.expression()))
    def visitExprFloor(self, ctx): return floor(self.visit(ctx.expression()))
    def visitExprRelational(self, ctx): return Integer(1)
    def visitExprAnd(self, ctx): return Integer(1)
    def visitExprOr(self, ctx): return Integer(1)
    def visitExprNot(self, ctx): return Integer(1)

    def _count_ops_in_expr(self, expr_ctx):
        count = 0
        if hasattr(expr_ctx, 'expression'):
            exprs = expr_ctx.expression()
            if isinstance(exprs, list):
                for e in exprs: count += self._count_ops_in_expr(e)
            elif exprs: count += self._count_ops_in_expr(exprs)
        if expr_ctx.getChildCount() > 1: count += 1
        return Integer(max(1, count))