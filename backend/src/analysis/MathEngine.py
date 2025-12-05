import re
import math
from sympy import symbols, Function, sympify, solve, roots, degree, O, oo, limit, simplify, log, Sum, Add, Mul, Max, Wild

class MathEngine:
    def __init__(self):
        self.n = symbols('n', integer=True, positive=True)
        self.T = Function('T')

    def _clean_expression(self, expr):
        """
        Cleans the expression to prioritize T(n) terms and remove unnecessary artifacts.
        """
        if expr is None: return 0
        
        # If it's a Max, prioritize the term with T
        if isinstance(expr, Max):
            # Check if any arg has T
            has_T = [arg for arg in expr.args if arg.has(self.T)]
            if has_T:
                # If multiple T terms, take the one with largest argument? 
                # For now, just take the first one found, or sum them?
                # Usually Max(T(n-1), T(n-2)) -> T(n-1) + T(n-2) for complexity? 
                # No, Max is Max. But for worst case analysis of branching, we usually sum them if we don't know?
                # But here we are cleaning for display/calculation.
                # Let's return the first T term found.
                return self._clean_expression(has_T[0])
            else:
                # If no T, return the max of args (simplified)
                return self._clean_expression(expr.args[0]) # Fallback
        
        if hasattr(expr, 'args') and expr.args:
            # If it's a function call T(...), keep it
            if isinstance(expr, Function) and expr.name == 'T':
                return expr
            
            # If it's a Sum, keep it
            if isinstance(expr, Sum):
                return expr
                
            # Recursively clean args
            # But be careful not to break structure
            # For Add/Mul, we might want to filter?
            pass

        return expr

    def get_recursive_part(self, expr):
        """Extracts the recursive branch from a Max expression."""
        if isinstance(expr, Max):
            for arg in expr.args:
                if arg.has(self.T): return self.get_recursive_part(arg)
            return expr
        
        if expr.is_Add:
            return self._clean_expression(expr)
            
        return expr

    def get_base_part(self, expr):
        """Extracts the base case cost (non-recursive branch) from a Max expression."""
        if isinstance(expr, Max):
            non_recursive_args = [arg for arg in expr.args if not arg.has(self.T)]
            if non_recursive_args:
                return Max(*non_recursive_args)
            return 0
        
        if expr.is_Add:
            new_args = [self.get_base_part(arg) for arg in expr.args]
            return Add(*new_args)
            
        if expr.is_Mul:
            new_args = [self.get_base_part(arg) for arg in expr.args]
            return Mul(*new_args)
            
        if expr.has(self.T):
            return 0
            
        return expr

    def solve_recurrence(self, total_cost):
        """
        Analyzes the total cost expression to determine complexity.
        """
        # 1. Extract terms
        # Assume total_cost is like T(n/b) + f(n) or T(n-1) + ...
        
        # Convert to string to check pattern? Or use SymPy structure.
        # Let's try to identify if it fits Master Theorem or Linear Recurrence.
        
        # Linear Recurrence: T(n) = c1*T(n-1) + ...
        # Master Theorem: T(n) = a*T(n/b) + f(n)
        
        terms = total_cost.as_ordered_terms() if hasattr(total_cost, 'as_ordered_terms') else [total_cost]
        
        # Check for Master Theorem pattern
        a = 0
        b = 0
        f_n = 0
        
        is_master = False
        is_linear = False
        
        # Helper to find T terms
        t_terms = []
        other_terms = []
        
        for term in terms:
            if term.has(self.T):
                t_terms.append(term)
            else:
                other_terms.append(term)
        
        f_n = Add(*other_terms)
        
        if not t_terms:
            # No recursion?
            return {"complexity": f_n, "details": {"type": "iterative"}}

        # Analyze T terms
        # Check for T(n/b)
        for term in t_terms:
            # term could be 2*T(n/2)
            coeff = 1
            if term.is_Mul:
                coeffs = [c for c in term.args if c.is_Number]
                if coeffs: coeff = coeffs[0]
                
            # Find the T function
            t_funcs = [atom for atom in term.atoms(Function) if atom.name == 'T']
            if t_funcs:
                t_func = t_funcs[0]
                arg = t_func.args[0]
                
                # Check arg pattern
                # n/b
                if arg.is_Mul or arg.is_Pow: # n/2 is n * 1/2
                    # Check if it is n * const
                    wild_b = symbols('b', cls=Wild)
                    # match = arg.match(self.n / wild_b) # SymPy match is tricky
                    
                    # Manual check
                    # arg = n * (1/b)
                    ratio = simplify(self.n / arg)
                    if ratio.is_constant() and ratio > 1:
                        b = ratio
                        a += coeff
                        is_master = True
                
                # n-k
                diff = simplify(self.n - arg)
                if diff.is_constant() and diff > 0:
                    is_linear = True
                    # We collect these for characteristic equation
        
        if is_master and not is_linear:
            return self._master_theorem(a, b, f_n)
            
        if is_linear:
            # Use characteristic equation solver
            # We need to pass the full list of terms that equal T(n) (conceptually T(n) - terms = 0)
            # But here 'terms' are the RHS of T(n) = ...
            return self._solve_characteristic_equation(t_terms)

        return {"complexity": total_cost, "details": {"type": "unknown"}}

    def _master_theorem(self, a, b, f_n):
        try:
            log_val = log(a, b)
            n_log = self.n ** log_val
            
            # Estructura de retorno base
            details = {
                "type": "master_theorem",
                "a": str(a),
                "b": str(b),
                "f_n": str(f_n),
                "log_val": str(log_val), # log_b(a)
                "case": "unknown"
            }

            if n_log == 0: 
                return {"complexity": f_n, "details": details}
            
            ratio = simplify(f_n / n_log)
            limit_val = ratio.limit(self.n, oo)
            
            # Caso 1: f(n) es polinómicamente menor que n^log_b(a)
            # Si f(n) / n^log_b(a) -> 0, entonces f(n) es O(n^{log_b a - epsilon})
            if limit_val == 0: 
                details["case"] = 1
                return {"complexity": n_log, "details": details}
            
            # Caso 3: f(n) es Omega(n^{log_b a + epsilon})
            # Si el límite es infinito
            if limit_val == oo:
                details["case"] = 3
                # Condición de regularidad a*f(n/b) <= c*f(n) para c < 1
                # Asumimos que se cumple para entradas estándar
                return {"complexity": f_n, "details": details}

            # Caso 2: f(n) es Theta(n^log_b(a) * log^k n)
            # Si el límite es una constante positiva
            if limit_val.is_number and limit_val > 0: 
                details["case"] = 2
                res = n_log * log(self.n, 2)
                return {"complexity": res, "details": details}
            
            return {"complexity": f_n, "details": details}
        except: return {"complexity": f_n, "details": None}

    def _solve_characteristic_equation(self, terms):
        """
        Resuelve recurrencias lineales homogéneas usando la ecuación característica.
        Forma: T(n) - c1*T(n-1) - c2*T(n-2) ... = 0
        """
        try:
            print(f"DEBUG: Solving characteristic equation for terms: {terms}")
            # Construir polinomio característico
            # r^k - c1*r^(k-1) - ... = 0
            # Mapeamos T(n-k) a r^(max_lag - k)
            
            lags = []
            coeffs = {} # lag -> coeff
            
            for term in terms:
                # Buscar T(n-k)
                t_calls = [atom for atom in term.atoms(Function) if atom.name == 'T']
                if t_calls:
                    arg = t_calls[0].args[0]
                    diff = simplify(self.n - arg)
                    if diff.is_constant() and diff > 0:
                        lag = int(diff)
                        lags.append(lag)
                        
                        # Extraer coeficiente
                        coeff = 1
                        if term.is_Mul:
                            c_list = [c for c in term.args if c.is_Number]
                            if c_list: coeff = c_list[0]
                        coeffs[lag] = coeff
            
            if not lags: return {"complexity": "Unknown", "details": None}
            
            max_lag = max(lags)
            r = symbols('r')
            
            # Polinomio: r^max_lag - sum(coeff * r^(max_lag - lag))
            poly = r**max_lag
            for lag, coeff in coeffs.items():
                poly -= coeff * r**(max_lag - lag)
                
            # Resolver raíces
            poly_roots = roots(poly)
            print(f"DEBUG: Roots found: {poly_roots}")
            
            # Encontrar la raíz dominante
            max_root = 0
            max_abs_val = -1
            
            for root in poly_roots:
                try:
                    val = root.evalf()
                    abs_val = abs(complex(val))
                except:
                    abs_val = 0
                
                if abs_val > max_abs_val:
                    max_abs_val = abs_val
                    max_root = root
            
            print(f"DEBUG: Max root: {max_root}")
            
            # Detectar Golden Ratio
            if "sqrt(5)" in str(max_root):
                res_str = "Θ(1.618^n)"
            else:
                big_o = O(max_root**self.n, (self.n, oo))
                res_str = str(big_o)
                
                res_str = res_str.replace(", (n, oo)", "")
                res_str = res_str.replace("O(", "Θ(")
                res_str = res_str.replace("**", "^")
                res_str = res_str.replace("log(1/n)", "log(n)") 
                res_str = res_str.replace("log(n)/log(2)", "log n")
            
            # Limpieza de Exponenciales
            if "exp(" in res_str:
                match_log = re.search(r'exp\((?:[0-9\.]+\*)?n\*log\(([0-9]+)\)\)', res_str)
                if match_log:
                    base = match_log.group(1)
                    res_str = f"Θ({base}^n)"
                
                match_num = re.search(r'exp\(([0-9\.]+)\*n\)', res_str)
                if match_num:
                    val = float(match_num.group(1))
                    base = round(math.exp(val), 2)
                    if base.is_integer(): base = int(base)
                    res_str = f"Θ({base}^n)"
            
            return {
                "complexity": res_str,
                "details": {
                    "type": "characteristic_equation",
                    "lags": lags,
                    "roots": [str(r) for r in poly_roots],
                    "dominant_root": str(max_root)
                }
            }
        except Exception as e: 
            print(f"DEBUG: Error in characteristic equation: {e}")
            return {"complexity": "Unknown Recurrence", "details": None}

    def format_complexity(self, complexity, use_theta=True):
        """Formatea la complejidad para que sea legible."""
        try:
            if hasattr(complexity, 'free_symbols') and self.n in complexity.free_symbols:
                 big_o = O(complexity, (self.n, oo))
                 complexity = big_o
        except: pass

        s = str(complexity)
        
        s = s.replace(", (n, oo)", "")
        s = s.replace("O(", "Theta(") if use_theta else s
        s = s.replace("Θ(", "Theta(") 

        s = s.replace("log(n)/log(2)", "log n")
        s = s.replace("log(n)", "log n")
        
        match_exp = re.search(r'exp\(n\s*\*\s*log\((.+?)\)\)', s)
        if match_exp:
            base = match_exp.group(1)
            # Reemplazar toda la expresión exp(...) por base^n
            s = s.replace(match_exp.group(0), f"({base})^n")

        # Reemplazo de Phi (Numero Aureo)
        s = s.replace("1/2 + sqrt(5)/2", "φ")
        s = s.replace("(1 + sqrt(5))/2", "φ")
        s = s.replace("sqrt(5)/2 + 1/2", "φ")
        s = s.replace("phi", "φ")
        s = s.replace("\\phi", "φ")

        # Reemplazo de sqrt
        s = s.replace("sqrt", "√")

        # Limpieza de potencias y multiplicaciones
        s = s.replace("**", "^")
        s = s.replace("*", " ")
        
        # Corrección de espacios dobles
        while "  " in s: s = s.replace("  ", " ")
        s = s.strip()
        
        # Caso Theta / O
        if "Theta" not in s and "O(" not in s:
            return f"Theta({s})" if use_theta else f"O({s})"
            
        return s

    def explain_recurrence(self, complexity_data, recurrence_eq_str):
        """
        Generates a didactic explanation for the solved recurrence.
        """
        if not isinstance(complexity_data, dict):
            return "No explanation available for this complexity."
            
        details = complexity_data.get("details")
        complexity = complexity_data.get("complexity")
        
        if not details:
            return "No detailed explanation available."
            
        explanation = []
        explanation.append(f"### Análisis de Recurrencia\n")
        explanation.append(f"**Ecuación Original:** `{recurrence_eq_str}`\n")
        
        # Clarify constant costs
        if "+" in recurrence_eq_str and not "log" in recurrence_eq_str:
             explanation.append("> **Nota:** Los términos constantes (ej: `+ c`) representan el costo fijo de las operaciones internas (comparaciones, sumas, retornos) en cada paso de la recursión.\n")
        
        type_ = details.get("type")
        
        if type_ == "master_theorem":
            a = details.get("a")
            b = details.get("b")
            f_n = details.get("f_n")
            case = details.get("case")
            log_val = details.get("log_val")
            
            explanation.append("#### 1. Identificación de Términos")
            explanation.append(f"- **a = {a}**: El número de subproblemas recursivos.")
            explanation.append(f"- **b = {b}**: El factor de reducción del tamaño de la entrada (n/{b}).")
            explanation.append(f"- **f(n) = {f_n}**: El costo de dividir el problema y combinar los resultados.")
            explanation.append("")
            
            explanation.append("#### 2. Método de Resolución: Teorema Maestro")
            explanation.append("Usamos el Teorema Maestro porque la recurrencia tiene la forma `T(n) = aT(n/b) + f(n)`.")
            explanation.append(f"Comparamos `f(n)` con `n^log_b(a)`.")
            explanation.append(f"- Calculamos `log_b(a) = log_{b}({a}) approx {float(sympify(log_val).evalf()):.2f}`.")
            explanation.append(f"- Por lo tanto, comparamos `f(n)` con `n^{log_val}`.")
            explanation.append("")
            
            explanation.append("#### 3. Paso a Paso")
            if case == 1:
                explanation.append(f"**Caso 1:** `f(n)` es polinómicamente menor que `n^log_b(a)`.")
                explanation.append(f"Esto significa que el costo de las hojas del árbol de recursión domina.")
                explanation.append(f"La complejidad está determinada por la cantidad de hojas.")
            elif case == 2:
                explanation.append(f"**Caso 2:** `f(n)` es similar a `n^log_b(a)`.")
                explanation.append(f"El costo es uniforme en todos los niveles del árbol de recursión.")
                explanation.append(f"Multiplicamos por un factor logarítmico `log n`.")
            elif case == 3:
                explanation.append(f"**Caso 3:** `f(n)` es polinómicamente mayor que `n^log_b(a)`.")
                explanation.append(f"El costo en la raíz domina sobre los subproblemas.")
                explanation.append(f"La complejidad es del orden de `f(n)`.")
            else:
                explanation.append("Caso desconocido o no aplicable directamente.")
                
            explanation.append("")
            explanation.append(f"#### 4. Resultado Final")
            explanation.append(f"La complejidad es **{self.format_complexity(complexity)}**.")
            explanation.append("> Para este tipo de algoritmos, los casos Mejor, Promedio y Peor suelen tener la misma complejidad asintótica.")

        elif type_ == "characteristic_equation":
            roots_list = details.get("roots")
            lags = details.get("lags")
            dom_root = details.get("dominant_root")
            
            explanation.append("#### 1. Identificación de Términos")
            explanation.append(f"La recurrencia depende de términos anteriores como: {', '.join([f'T(n-{k})' for k in lags])}.")
            explanation.append("Esto indica una **Recurrencia Lineal Homogénea**.")
            explanation.append("")
            
            explanation.append("#### 2. Método de Resolución: Ecuación Característica")
            explanation.append("Transformamos la recurrencia en un polinomio característico sustituyendo `T(n)` por `r^n`.")
            explanation.append(f"Las raíces de este polinomio determinan la tasa de crecimiento.")
            explanation.append("")
            
            explanation.append("#### 3. Paso a Paso")
            explanation.append(f"- Encontramos las raíces del polinomio: {', '.join(roots_list)}.")
            if dom_root:
                explanation.append(f"- La **raíz dominante** es `{dom_root}`.")
            explanation.append("- Esta raíz dicta la base del crecimiento exponencial.")
            
            # Check for Phi
            if any("sqrt(5)" in r for r in roots_list):
                explanation.append("- Notamos la presencia de `(1+sqrt(5))/2` (Phi approx 1.618), típico de Fibonacci.")
            
            explanation.append("")
            explanation.append(f"#### 4. Resultado Final")
            explanation.append(f"La complejidad es **{self.format_complexity(complexity)}**.")
            explanation.append("> Dado que la estructura recursiva es fija (siempre hace las mismas llamadas), la complejidad es **Exponencial** en todos los casos (Mejor, Promedio y Peor).")
            
        elif type_ == "linear_recurrence":
            subtype = details.get("subtype")
            a = details.get("a")
            
            explanation.append("#### 1. Análisis")
            explanation.append(f"Es una recurrencia lineal simple.")
            if subtype == "exponential":
                explanation.append(f"Cada paso genera `{a}` llamadas recursivas con una reducción constante (resta).")
                explanation.append("Esto lleva a un crecimiento exponencial.")
            elif subtype == "polynomial":
                explanation.append("Solo hay 1 llamada recursiva por paso (`a=1`).")
                explanation.append("Esto se comporta como un bucle, sumando el costo `f(n)` en cada paso.")
            
            explanation.append("")
            explanation.append(f"#### 2. Resultado Final")
            explanation.append(f"La complejidad es **{self.format_complexity(complexity)}**.")
            
        else:
            explanation.append("No se pudo generar una explicación detallada para este tipo de recurrencia.")
            
        return "\n".join(explanation)

    def explain_iterative(self, complexity_expr):
        """
        Generates a didactic explanation for iterative algorithms (loops).
        """
        explanation = []
        explanation.append(f"### Análisis Iterativo\n")
        
        s_expr = str(complexity_expr)
        
        explanation.append("#### 1. Desglose de Operaciones")
        if "Sum" in s_expr:
            explanation.append("El algoritmo contiene **ciclos** (bucles) que se modelan matemáticamente como sumatorias.")
            
            # Simple heuristic to detect nesting
            count_sum = s_expr.count("Sum")
            if count_sum > 1:
                explanation.append(f"- Se detectaron **{count_sum} ciclos anidados** (o secuenciales complejos).")
                explanation.append("- Esto generalmente implica multiplicar las iteraciones de cada nivel.")
            else:
                explanation.append("- Se detectó un **ciclo simple**.")
                explanation.append("- El costo es la suma del cuerpo del ciclo por el número de iteraciones.")
        else:
            explanation.append("El algoritmo es **secuencial** (sin ciclos complejos detectados en la expresión final).")
            explanation.append("Se compone de una serie de operaciones simples.")

        explanation.append("")
        explanation.append("#### 2. Cálculo Exacto")
        explanation.append(f"La expresión matemática exacta del costo es:")
        explanation.append(f"`{s_expr}`")
        
        # Try to simplify/expand if it's a Sum
        try:
            if hasattr(complexity_expr, 'doit'):
                expanded = complexity_expr.doit()
                explanation.append(f"Al resolver las sumatorias, obtenemos:")
                explanation.append(f"`{expanded}`")
        except: pass

        explanation.append("")
        explanation.append("#### 3. Resultado Final")
        explanation.append(f"La complejidad asintótica es **{self.format_complexity(complexity_expr)}**.")
        
        return "\n".join(explanation)

    def sum_loop(self, body_cost, var, start, end):
        """
        Calculates the summation of body_cost from start to end.
        """
        # Ensure symbols are correct
        # var is string, convert to symbol
        k = symbols(var, integer=True)
        
        # body_cost might contain k
        # If body_cost is Integer or constant, sum is count * body
        
        # We use SymPy Sum
        s = Sum(body_cost, (k, start, end))
        return s