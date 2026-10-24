# Faça um programa para ler um valor inteiro que representa o tamanho de
# uma Lista e a seguir atribua para as posiões pares desta lista o valor 
# 0 (zero) e para as posições ímpares o valor 1 (um). Finalizando,
# mostre os valores da Lista como mostrado na coluna 'Resultados'.

# Resultados
# 7
# {0, 1, 0, 1, 0, 1, 0}
# 5
# {0, 1, 0, 1, 0}
# 10
# {0, 1, 0, 1, 0, 1, 0, 1, 0, 1}


def returnNumberOrThrowIfNot(a) -> int:
    try:
        a = int(a)
    except (ValueError, TypeError):
        raise TypeError(f"Variable '{a}' should be a number") from None

    return a

tamanho_lista = returnNumberOrThrowIfNot(input())

resposta = "{";
for i in range(tamanho_lista):
    resposta += f"{'1' if i % 2 else '0'}"
    if i != (tamanho_lista - 1):
        resposta += ", "
resposta += "}"

print(resposta)

 

