from __future__ import print_function

while True:
    cantidad = int(raw_input())
    if cantidad == 0:
        break
    else:
        cadena = raw_input()
        lista = []
        for i in range(0, len(cadena), cantidad):
            lista.append(cadena[i: i + cantidad])
        for i in range(len(lista)):
            if i % 2 != 0:
                lista[i] = ''.join(reversed(lista[i]))
        for i in range(cantidad):
            for pedazo in lista:
                print(pedazo[i], end='')
        print()
