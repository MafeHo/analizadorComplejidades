# src/analysis/MathEngine.py

from sympy import symbols, Sum, Function, O, oo, log, sympify, Integer, Symbol, simplify, Add, Mul, Pow, Max, roots
import math
import re

class MathEngine:
    def __init__(self):
        self.n = symbols('n', integer=True, positive=True)
        self.T = Function('T')
    
    def sum_loop(self, body_cost, iterator_var_name, start_expr, end_expr):
        """Calcula sumatoria exacta."""
        try:
            i = symbols(str(iterator_var_name), integer=True)
            s = sympify(start_expr)
            e = sympify(end_expr)
            
            # Sustituir la variable genérica por la variable de sumatoria (entera)
            generic_i = Symbol(str(iterator_var_name))
            if hasattr(body_cost, 'subs'):
                body_cost = body_cost.subs(generic_i, i)
            
            sigma_body = Sum(body_cost, (i, s, e)).doit()
            header_cost = (e - s + 2)
            return simplify(sigma_body + header_cost)
        except: return self.n 

    def solve_recurrence(self, complexity_expr):
        """Resuelve T(n) analizando matemáticamente el argumento."""
        # 1. Limpieza
        clean_expr = self._clean_expression(complexity_expr)
        expr = simplify(clean_expr)
        
        # 2. Análisis de Términos
        terms = expr.args if expr.is_Add else [expr]
        
        # Recolectar a (coeficiente) y argumentos de T
        a = 0
        target_args = set()
        non_recursive_terms = []
        
        for term in terms:
            # Buscar T dentro del término
            t_calls = [atom for atom in term.atoms(Function) if atom.name == 'T']
            
            if not t_calls:
                non_recursive_terms.append(term)
                continue
            
            # Asumimos una forma a * T(arg)
            coeff = 1
            if term.is_Mul:
                coeffs = [c for c in term.args if c.is_Number]
                if coeffs: coeff = coeffs[0]
            
            a += coeff
            target_args.add(t_calls[0].args[0])

        # f(n) es el costo resto
        f_n = Add(*non_recursive_terms) if non_recursive_terms else Integer(0)
        
        if a == 0: return {"complexity": expr, "details": None} # Es iterativo
        
        # Si hay múltiples argumentos diferentes (ej: n-1 y n-2), usar Ecuación Característica
        if len(target_args) > 1:
             return self._solve_characteristic_equation(terms)

        target_arg = list(target_args)[0]
        
        # --- DETECCIÓN MATEMÁTICA DEL PATRÓN ---
        
        # Prueba 1: ¿Es resta? (Hanoi, Fibonacci linealizado)
        # Verificamos si (n - argumento) es una constante positiva
        diff = simplify(self.n - target_arg)
        if diff.is_constant() and diff > 0:
            k = diff
            # Regla de apuntes:
            # Si a > 1 (ej: 2) -> Exponencial a^(n/k)
            if a > 1: 
                res = Pow(a, self.n / k)
                return {"complexity": res, "details": {"type": "linear_recurrence", "subtype": "exponential", "a": a, "k": k}}
            # Si a = 1 -> Polinomial n * f(n)
            res = self.n * f_n
            return {"complexity": res, "details": {"type": "linear_recurrence", "subtype": "polynomial", "a": a, "f_n": str(f_n)}}

        # Prueba 2: ¿Es división? (MergeSort, Binaria)
        # Verificamos si (n / argumento) es una constante positiva > 1
        ratio = simplify(self.n / target_arg)
        if ratio.is_constant() and ratio > 1:
            b = ratio
            return self._master_theorem(a, b, f_n)

        # Prueba 3: Ecuación Característica (Fibonacci, Linear Homogeneous)
        # Buscamos patrón: T(n) = c1*T(n-1) + c2*T(n-2) + ...
        # Recolectamos todos los términos T(n-k)
        if str(expr).count("T") > 1:
            return self._solve_characteristic_equation(terms)

        return {"complexity": expr, "details": None}

    def _clean_expression(self, expr):
        """Elimina Max() quedándose con la rama recursiva."""
        if isinstance(expr, Max):
            # Prioridad: argumento con T
            for arg in expr.args:
                if arg.has(self.T): return self._clean_expression(arg)
            return self._clean_expression(expr.args[0])
        
        if expr.is_Add or expr.is_Mul:
            new_args = [self._clean_expression(arg) for arg in expr.args]
            return expr.func(*new_args)
        return expr

    def get_recursive_part(self, expr):
        """Extracts the recursive branch from a Max expression."""
        if isinstance(expr, Max):
            # Return the argument that contains T
            for arg in expr.args:
                if arg.has(self.T): return self.get_recursive_part(arg)
            # If neither has T (unlikely if we are here), return the first one or max
            return expr
        
        if expr.is_Add:
            # For addition, we want to keep the parts that are recursive OR constant overhead associated with it
            # But strictly speaking, if we have Max(Recursive, Base) + Overhead, 
            # the recursive part is Recursive + Overhead.
            # However, simpler approach: clean the expression using _clean_expression logic which already favors T
            return self._clean_expression(expr)
            
        return expr

    def get_base_part(self, expr):
        """Extracts the base case cost (non-recursive branch) from a Max expression."""
        if isinstance(expr, Max):
            # Return the argument that DOES NOT contain T
            # If multiple, take the max of them? Usually one is recursive, one is base.
            non_recursive_args = [arg for arg in expr.args if not arg.has(self.T)]
            if non_recursive_args:
                return Max(*non_recursive_args)
            
            # If all have T, then there is no base case path in this Max?
            return Integer(0)
        
        if expr.is_Add:
            # If we have A + B, and A has Max(Rec, Base), then Base part is Base + B
            # We need to traverse and replace Max(Rec, Base) with Base.
            new_args = [self.get_base_part(arg) for arg in expr.args]
            return Add(*new_args)
            
        if expr.is_Mul:
            new_args = [self.get_base_part(arg) for arg in expr.args]
            return Mul(*new_args)
            
        # If it's a T(n) call, it contributes 0 to the base case cost? 
        # Or should we say the base case implies T(n) is not called?
        # If we are evaluating the cost of the base case path, T(n) should not be there.
        if expr.has(self.T):
            return Integer(0)
            
        return expr

    def _master_theorem(self, a, b, f_n):
        try:
            log_val = log(a, b)
            n_log = self.n ** log_val
            
            # Estructura de retorno base
            details = {
                "type": "master_theorem",
                "a": a,
                "b": b,
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
            # Nota: Los términos en 'terms' son positivos en la ecuación T(n) = ...
            # Por lo tanto, en la ecuación característica r^k = ..., los signos se mantienen.
            
            poly = r**max_lag
            for lag, coeff in coeffs.items():
                poly -= coeff * r**(max_lag - lag)
                
            # Resolver raíces
            poly_roots = roots(poly)
            print(f"DEBUG: Roots found: {poly_roots}")
            
            # Encontrar la raíz dominante (mayor valor absoluto)
            max_root = 0
            max_abs_val = -1
            
            for root in poly_roots:
                # Aproximación numérica para comparación
                try:
                    val = root.evalf()
                    abs_val = abs(complex(val))
                except:
                    abs_val = 0
                
                if abs_val > max_abs_val:
                    max_abs_val = abs_val
                    max_root = root
            
            print(f"DEBUG: Max root: {max_root}")
            
            # Construir la complejidad final
            # O(root^n)
            # Para Fibonacci, max_root es (1+sqrt(5))/2 approx 1.618
            big_o = O(max_root**self.n, (self.n, oo))
            res_str = str(big_o)
            
            # Limpieza básica
            res_str = res_str.replace(", (n, oo)", "")
            res_str = res_str.replace("O(", "Θ(")
            res_str = res_str.replace("**", "^")
            res_str = res_str.replace("log(1/n)", "log(n)") 
            res_str = res_str.replace("log(n)/log(2)", "log n")
            
            # Limpieza de Exponenciales (exp(k*n) -> base^n)
            if "exp(" in res_str:
                # Busca exp( numeritos * n * log(base) ) o variaciones
                # Caso Hanoi: exp(1.0*n*log(2))
                match_log = re.search(r'exp\((?:[0-9\.]+\*)?n\*log\(([0-9]+)\)\)', res_str)
                if match_log:
                    base = match_log.group(1)
                    res_str = f"Θ({base}^n)"
                
                # Caso Genérico: exp(0.693*n) -> e^0.693 = 2
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
            return "Unknown Recurrence"

    def format_complexity(self, complexity):
        """Formatea la complejidad para que sea legible."""
        # Intenta simplificar a Big-O si es una expresión matemática compleja
        try:
            if hasattr(complexity, 'free_symbols') and self.n in complexity.free_symbols:
                 # Calcular Big-O
                 big_o = O(complexity, (self.n, oo))
                 complexity = big_o
        except: pass

        s = str(complexity)
        
        # Limpieza de Big-O de SymPy
        s = s.replace(", (n, oo)", "")
        s = s.replace("O(", "Theta(")
        s = s.replace("Θ(", "Theta(") # Unificar a ASCII

        # Limpieza de logaritmos
        s = s.replace("log(n)/log(2)", "log n")
        s = s.replace("log(n)", "log n")
        
        # Limpieza de Exponenciales complejos: exp(n*log(X)) -> X^n
        # Busca exp(n*log(CualquierCosa))
        match_exp = re.search(r'exp\(n\s*\*\s*log\((.+?)\)\)', s)
        if match_exp:
            base = match_exp.group(1)
            # Reemplazar toda la expresión exp(...) por base^n
            s = s.replace(match_exp.group(0), f"({base})^n")

        # Reemplazo de Phi (Numero Aureo)
        # Variaciones comunes de SymPy
        s = s.replace("1/2 + sqrt(5)/2", "phi")
        s = s.replace("(1 + sqrt(5))/2", "phi")
        s = s.replace("sqrt(5)/2 + 1/2", "phi")

        # Reemplazo de sqrt
        s = s.replace("sqrt", "√")

        # Limpieza de potencias y multiplicaciones
        s = s.replace("**", "^")
        s = s.replace("*", " ")
        
        # Corrección de espacios dobles
        while "  " in s: s = s.replace("  ", " ")
        s = s.strip()
        
        # Caso Theta
        if "Theta" not in s and "O(" not in s:
            return f"Theta({s})"
            
        return s

    def explain_recurrence(self, complexity_data, recurrence_eq_str):
        """
        Generates a didactic explanation for the solved recurrence.
        
        Args:
            complexity_data (dict): The result from solve_recurrence.
            recurrence_eq_str (str): The raw equation string (e.g. "T(n) = 2*T(n/2) + n").
            
        Returns:
            str: A markdown string with the explanation.
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
        
        Args:
            complexity_expr: The sympy expression representing the total cost.
            
        Returns:
            str: A markdown string with the explanation.
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