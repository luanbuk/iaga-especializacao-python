
valor = input()

valor_fragmentado = [f"{fragmento} " for fragmento in list(valor)]
for i in range(3):
    print("".join(valor_fragmentado))
        
