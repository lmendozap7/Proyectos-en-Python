from __future__ import print_function
arreglo = raw_input().split()
longitud = len(arreglo) - 1
for i in range(longitud):
    if 'kroketten'.upper() == arreglo[i].upper():
        print('croqueta ', end='')
    else:
        print(arreglo[i] + ' ', end='')
if arreglo[longitud].upper() == 'kroketten'.upper():
    print('croqueta', end='')
else:
    print(arreglo[longitud], end='')
