from __future__ import print_function
from string import ascii_lowercase

abecedario = ascii_lowercase
while True:
    cadena = raw_input()
    if cadena == '*':
        break
    elif cadena.isalpha():
        num = 0
        alreves = ''.join(reversed(cadena))
        for i in range(len(cadena)):
            num += (abecedario.index(alreves[i]) + 1) * 26 ** i
        print(cadena.ljust(22, ' '), end='')
        print("{:,}".format(num))
    else:
        numero = long(cadena)
        salida = []
        while numero > 0:
            auxiliar = numero % 26
            numero /= 26
            salida.append(str(abecedario[auxiliar - 1]))
        print(''.join(reversed(salida)).ljust(22, ' '), end='')
        print("{:,}".format(long(cadena)))
