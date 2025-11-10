# src/analysis/CostCalculator.py

from ..parsing.PseudoCodeAnalyzerVisitor import PseudoCodeAnalyzerVisitor
from ..parsing.PseudoCodeAnalyzerParser import PseudoCodeAnalyzerParser
from ..llm_integration.LLM_Client import LLMClient

# Una clase para contener el resultado del análisis
class AnalysisResult:
    def __init__(self, worst_case=None, best_case=None, avg_case=None, reasoning=""):
        self.worst_case = worst_case # Notación O
        self.best_case = best_case   # Notación Omega (Ω)
        self.avg_case = avg_case     # Notación Theta (Θ)
        self.reasoning = reasoning

class CostCalculator(PseudoCodeAnalyzerVisitor):
    def __init__(self, llm_client):
        # Almacena el cliente LLM para resolver sumatorias/recurrencias
        self.llm_client = llm_client 
        self.cost_map = {}  # Mapea IDs de subrutinas a su complejidad T(n)
        self.current_T_n = "1" # Costo de la línea actual
        self.algorithm_definitions = {} # Para almacenar el pseudocódigo de cada subrutina

    # -------------------------------------------------------------
    # Método Principal (Subrutinas)
    # -------------------------------------------------------------
    def visitSubroutine_declaration(self, ctx:PseudoCodeAnalyzerParser.Subroutine_declarationContext):
        # 1. Obtener el nombre del algoritmo (ej. 'MergeSort')
        algo_name = ctx.ID(0).getText()
        
        # 2. Calcular el costo total T(n) del cuerpo del algoritmo
        # La visita a statement_list devolverá la suma total de costos del cuerpo
        body_cost = self.visit(ctx.statement_list()) 

        # 3. Almacenar el resultado (Simplificado, la lógica real es más compleja)
        # Aquí se debería llamar a un simplificador para obtener O, Ω, Θ
        self.cost_map[algo_name] = body_cost 
        print(f"Algoritmo {algo_name} tiene un costo T(n) preliminar: {body_cost}")
        
        return AnalysisResult(worst_case=body_cost) # Devuelve un objeto resultado

    # -------------------------------------------------------------
    # Manejo de Bloques de Sentencias (Suma de Costos)
    # -------------------------------------------------------------
    def visitStatement_list(self, ctx:PseudoCodeAnalyzerParser.Statement_listContext):
        total_cost = []
        for statement_ctx in ctx.statement():
            # Cada visita devuelve el costo de esa sentencia
            costo_sentencia = self.visit(statement_ctx)
            total_cost.append(str(costo_sentencia))
            
        # Retorna la representación simbólica de la suma de costos
        return " + ".join(total_cost)

    # -------------------------------------------------------------
    # Sentencias O(1)
    # -------------------------------------------------------------
    def visitAssignment(self, ctx:PseudoCodeAnalyzerParser.AssignmentContext):
        # Asignaciones, operaciones aritméticas, accesos a arreglos/objetos son O(1)
        # El costo es 1 unidad de tiempo.
        return 1

    # -------------------------------------------------------------
    # Control de Flujo (IF/ELSE)
    # -------------------------------------------------------------
    def visitIf_statement(self, ctx:PseudoCodeAnalyzerParser.If_statementContext):
        # 1. Costo de la condición (asumimos O(1) por ahora)
        cost_condition = 1
        
        # 2. Costo del bloque THEN (Bloque obligatorio)
        cost_then = self.visit(ctx.statement_list(0))
        
        # 3. Costo del bloque ELSE (Bloque opcional)
        cost_else = 0
        if ctx.ELSE():
            cost_else = self.visit(ctx.statement_list(1))
            
        # Peor caso (O): Costo de la condición + el camino más caro
        worst_case = f"{cost_condition} + max({cost_then}, {cost_else})"
        
        # Mejor caso (Ω): Costo de la condición + el camino menos caro
        best_case = f"{cost_condition} + min({cost_then}, {cost_else})"
        
        # Para el cálculo posterior de O, Ω, Θ, retornamos la estructura
        return {"O": worst_case, "Ω": best_case}


    # -------------------------------------------------------------
    # Control de Flujo (FOR Loop)
    # -------------------------------------------------------------
    def visitFor_loop(self, ctx:PseudoCodeAnalyzerParser.For_loopContext):
        # Asumimos que podemos obtener los límites y el cuerpo ya tiene un costo C.
        
        # 1. Obtener límites (Simplificado: n es el límite superior)
        start_expr = self.visit(ctx.expression(0)) # Expresión de inicio
        end_expr = self.visit(ctx.expression(1))   # Expresión de límite
        
        # 2. Costo del cuerpo del loop
        cost_body = self.visit(ctx.statement_list(0))
        
        # 3. Plantear la sumatoria simbólica 
        # Ejemplo de sumatoria que el LLM debe resolver:
        summation_expression = (
            f"Resolver la sumatoria: Sumatoria desde i = {start_expr} hasta {end_expr} "
            f"del costo total: ({cost_body}). Asume que el límite superior 'n' es la entrada."
        )

        # 4. Llamar al LLM para resolver la sumatoria (EL TRABAJO DURO)
        print("  > Solicitando resolución de sumatoria al LLM...")
        llm_response = self.llm_client.solve_equation("sumatoria", summation_expression)
        
        # 5. Se debe analizar la respuesta del LLM para extraer O, Ω, Θ.
        # Por simplicidad, retornamos la respuesta bruta del LLM para el costo T(n)
        return llm_response

    # Implementar de forma similar: visitWhile_loop y visitRepeat_loop
    # La dificultad aquí es determinar la condición de terminación, que a menudo requiere 
    # inferencia semántica compleja que el LLM podría asistir.
    
    # -------------------------------------------------------------
    # Control de Flujo (Llamadas: Recursión/Subrutinas)
    # -------------------------------------------------------------
    def visitCall_statement(self, ctx:PseudoCodeAnalyzerParser.Call_statementContext):
        called_name = ctx.ID().getText()
        
        # Lógica para identificar la recurrencia: 
        # Si 'called_name' es el mismo que el algoritmo actual, ¡es recursión!
        # Aquí la lógica real debe ser más sofisticada, pero simplificamos para el ejemplo.
        
        # Si es una llamada a sí mismo y tiene una división en el problema (ej. n/2),
        # Se plantea la Relación de Recurrencia
        
        # Ejemplo de Relación de Recurrencia que el LLM debe resolver:
        recurrence_relation = (
            "Resolver la siguiente relación de recurrencia usando el Teorema Maestro o "
            "sustitución: T(n) = 2*T(n/2) + n."
        )

        # 4. Llamar al LLM para resolver la recurrencia (EL TRABAJO DURO)
        print("  > Solicitando resolución de recurrencia al LLM...")
        llm_response = self.llm_client.solve_equation("relación de recurrencia", recurrence_relation)
        
        return llm_response