# Faça um programa para ler um valor inteiro que representa o tamanho (variável “n”) 
# de uma primeira Lista e a seguir leia todos os “n” elementos desta Lista. 
# E, também, construa uma segunda lista onde seus elementos são assim definidos: 
# a) se o elemento da primeira lista for um valor negativo, armazenar na segunda 
# lista o valor -1 (menos um); b) se o elemento da primeira lista for o valor 
# neutro (zero), armazenar na segunda lista o valor 0 (zero); e, c) se o elemento 
# da primeira lista for um valor positivo, armazenar na segunda lista o valor 
# 1 (um). Finalizando, mostre os valores das Listas como mostrado na coluna 
# 'Resultados'.

# Input
# 5
# 0
# -10
# 10
# 10
# 0
# Resultados
# [0, -10, 10, 10, 0]
# [0, -1, 1, 1, 0]

def readInputAsNumberOrThrow() -> int:
    try:
        a = int(input())
    except (ValueError, TypeError):
        raise TypeError(f"Input '{a}' should be a number") from None

    return a

def lerNNumeros(tamanho_lista):
    numeros = []
    # numeros = [1,2,3,4,5,6,7]
    for i in range(tamanho_lista):
        numeros.append(readInputAsNumberOrThrow())
    return numeros

valor_base = readInputAsNumberOrThrow()
numeros = lerNNumeros(valor_base)

lista_final = []
for i in range(valor_base):
    if numeros[i] == 0:
        lista_final.append(0)
    if numeros[i] > 0:
        lista_final.append(1)
    if numeros[i] < 0:
        lista_final.append(-1)

print(numeros)
print(lista_final)

