from __future__ import print_function
import string

alfabeto = string.ascii_uppercase
while True:
    linea = raw_input()
    if linea == '#':
        break
    cambio = ord(linea[len(linea) - 1]) - 65
    linea = linea[:len(linea) - 1]
    alfCambiado = alfabeto[cambio:] + alfabeto[:cambio]
    for letra in linea:
        if letra.isupper():
            print(alfabeto[alfCambiado.index(letra)], end='')
        elif letra.islower():
            print(alfabeto[alfCambiado.index(letra.upper())].lower(), end='')
        else:
            print(letra, end='')
    print()
