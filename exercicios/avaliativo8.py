# Faça um programa para ler do teclado 7 (sete) valores inteiros e os 
# armazene em uma Lista. Em seguida, deverão ser mostrados na 
# tela do computador: todos os elementos da Lista e os menor e maior 
# elementos desta Lista com as suas respectivas posições. 
# Observe o resultado final na coluna “Resultados”.

def readInputAsNumberOrThrow() -> int:
    try:
        a = int(input())
    except (ValueError, TypeError):
        raise TypeError(f"Input '{a}' should be a number") from None

    return a

def lerSeteNumeros():
    numeros = []
    # numeros = [1,2,3,4,5,6,7]
    for i in range(7):
        numeros.append(readInputAsNumberOrThrow())
    return numeros

def printNumeros(numeros):
    for i in range(len(numeros)):
        print(f"x[{i}] = {numeros[i]}") 

def encontrarMenorMaior(numeros):
    menor_valor, menor_pos = 99999999999999999, 99999999999999999
    maior_valor, maior_pos = -99999999999999999, -99999999999999999

    for i in range(len(numeros)):
        if numeros[i] > maior_valor:
            maior_valor = numeros[i]
            maior_pos = i

        if numeros[i] < menor_valor:
            menor_valor = numeros[i]
            menor_pos = i

    return menor_pos, menor_valor, maior_pos, maior_valor
            
numeros = lerSeteNumeros()
printNumeros(numeros)

menor_pos, menor_valor, maior_pos, maior_valor = encontrarMenorMaior(numeros)

print(f"Menor elemento, x[{menor_pos}] = {menor_valor}")
print(f"Maior elemento, x[{maior_pos}] = {maior_valor}")