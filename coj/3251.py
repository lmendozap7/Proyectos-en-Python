from __future__ import print_function

numero = raw_input()
contador = 0
longitud = len(numero)
if numero.__contains__('0'):
    for i in range(longitud):
        contador += int(numero[i])
    if contador % 3 == 0:
        numero = sorted(numero)
        for i in range(longitud - 1, -1, -1):
            print(numero[i], end='')
    else:
        print('-1')
else:
    print('-1')
