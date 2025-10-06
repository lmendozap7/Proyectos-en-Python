def mayor_digito(cadena):
    caracter = '0'
    for i in cadena:
        if i > caracter:
            caracter = i
    return int(caracter) + 1


for i in range(int(raw_input())):
    numero = raw_input()
    menor = long(numero)
    for j in range(mayor_digito(numero), 11):
        nuevo = long(numero, j)
        if menor > nuevo:
            menor = nuevo
    if menor < 4294967296:
        print(menor)
    else:
        print('-1')