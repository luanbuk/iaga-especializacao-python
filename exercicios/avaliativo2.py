import numbers;

def returnNumberOrThrowIfNot(a):
    try:
        a = int(a)
    except (ValueError, TypeError):
        raise TypeError(f"Variable '{a}' should be an int") from None

    return a

valor = returnNumberOrThrowIfNot(input());
lista_fixa = [10, 2, 7, 8, 5, 3, 22, 17, 18]

resposta = "{"

encontrado_posicao = -1
for i in range(len(lista_fixa)):
    valor_posicao = lista_fixa[i];
    resposta += f"{i}:{valor_posicao}"
    if i != len(lista_fixa) - 1:
        resposta += ", "
    if valor_posicao == valor:
        encontrado_posicao = i

resposta += "}"

print(resposta)

if encontrado_posicao == -1:
    print(f"Item: {valor}, \"nao\" foi encontrado.")
else:
    print(f"Item: {valor}, foi encontrado na posicao {encontrado_posicao}.")
