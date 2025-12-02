from strands import Tool

def calculate_expression(expr: str):
    try:
        return eval(expr)
    except Exception:
        return "Erro ao calcular expressão"

calculator_tool = Tool(
    name="calculator",
    description="Resolve expressões matemáticas simples.",
    func=lambda query: calculate_expression(query)
)
