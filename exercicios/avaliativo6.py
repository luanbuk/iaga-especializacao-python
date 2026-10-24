import re

valor = input()
palavras = [re.sub(r'[^a-zA-Z0-9]', '', palavra) for palavra in valor.split(' ')]

print(f"Existem {len(palavras)} palavras, são elas:\n")

for i in range(len(palavras)):
    print(f"{i + 1}a. palavra = {palavras[i]}")
