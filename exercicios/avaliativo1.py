import numbers;

def returnNumberOrThrowIfNot(a):
    try:
        a = float(a)
    except (ValueError, TypeError):
        raise TypeError(f"Variable '{a}' should be a number") from None

    if not isinstance(a, numbers.Number):
        raise TypeError(f"Variable '{a}' should be a number")

    return a

valor_produto = returnNumberOrThrowIfNot(input())
valor_desconto = valor_produto * 0.1
valor_final = valor_produto - valor_desconto

print(f"Valor do Produto  = {valor_produto:.2f}")
print(f"Valor do Desconto = {valor_desconto:.2f}")
print(f"Valor Final       = {valor_final:.2f}")