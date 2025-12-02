def calculate_expression(expr: str):
    try:
        return eval(expr)
    except Exception:
        return "Erro ao calcular expressão"
