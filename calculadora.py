# calculadora.py
def calculadora_simple(a, b, operador):
    # Validación de entradas
    if not isinstance(a, (int, float)):
        return "Error: 'a' no es número"
    if not isinstance(b, (int, float)):
        return "Error: 'b' no es número"
    
    # Procesamiento según operador
    if operador == '+':
        return a + b
    elif operador == '-':
        return a - b
    elif operador == '*':
        return a * b
    elif operador == '/':
        if b == 0:
            return "Error: División/0"
        return a / b
    else:
        return "Error: Operador inválido"