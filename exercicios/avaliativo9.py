# Faça um programa para ler um valor inteiro (variável “a”) e a 
# seguir construa uma Lista com 10 (dez) posições (variável “x”) 
# com o resultado da seguinte expressão:
# x[i] = a + i; para todo “i” variando de 0 até 9.

# Ex: 
# Input 5
# Resultados
# x[0] = 5 + 0 = 5
# x[1] = 5 + 1 = 6
# x[2] = 5 + 2 = 7
# x[3] = 5 + 3 = 8
# x[4] = 5 + 4 = 9
# x[5] = 5 + 5 = 10
# x[6] = 5 + 6 = 11
# x[7] = 5 + 7 = 12
# x[8] = 5 + 8 = 13
# x[9] = 5 + 9 = 14

def readInputAsNumberOrThrow() -> int:
    try:
        a = int(input())
    except (ValueError, TypeError):
        raise TypeError(f"Input '{a}' should be a number") from None

    return a

valor_base = readInputAsNumberOrThrow()

for i in range(10):
    print(f"x[{i}] = {valor_base} + {i} = {valor_base + i}")
