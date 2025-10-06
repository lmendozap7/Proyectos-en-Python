casos = int(raw_input())
for i in range(casos):
    cadena = raw_input()
    while len(cadena) > 1:
        contador = 0
        for letra in cadena:
            contador += int(letra)
        cadena = str(contador)
    print(cadena)
