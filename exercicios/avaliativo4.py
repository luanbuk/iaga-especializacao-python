
def returnNumberOrThrowIfNot(a):
    try:
        a = int(a)
    except (ValueError, TypeError):
        raise TypeError(f"Variable '{a}' should be a number") from None

    return a


tamanho_matriz = returnNumberOrThrowIfNot(input())

linha = ""
for i in range(tamanho_matriz):
    for j in range(tamanho_matriz):
        if i == 0 or i == (tamanho_matriz -1) or j == 0 or j == (tamanho_matriz - 1):
            linha += "* "
        else:
            linha += "@ "
    print(linha)
    linha = ""