import numbers;

def returnNumberOrThrowIfNot(a):
    try:
        a = float(a)
    except (ValueError, TypeError):
        raise TypeError(f"Variable '{a}' should be a number") from None

    return a

valor_produto = returnNumberOrThrowIfNot(input())
valor_limiar = 5000.00
valor_porcentagem = 0.15 if valor_produto >= valor_limiar else 0.1
valor_desconto = valor_produto * valor_porcentagem
valor_final = valor_produto - valor_desconto

print(f"Valor do Produto        = R$ {valor_produto:.2f}")
print(f"Valor do Desconto ({valor_porcentagem * 100:.0f}%) = R$ {valor_desconto:.2f}")
print(f"Valor Final             = R$ {valor_final:.2f}")