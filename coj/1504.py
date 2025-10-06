casos = int(raw_input())
for i in range(casos):
    contador = 0
    a, b = map(int, raw_input().split(" "))
    for j in range(a, b + 1):
        cadena = str(j)
        if '0' in cadena or '2' in cadena or '4' in cadena or '6' in cadena or '8' in cadena:
            contador += 1
    print contador