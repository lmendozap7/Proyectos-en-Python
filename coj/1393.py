base, exponente = map(long, raw_input().split())
cadena = str(base ** exponente)
longitud = len(cadena)
contador = 0
while contador < longitud:
    print(cadena[contador:contador + 70])
    contador += 70