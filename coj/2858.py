from __future__ import print_function

linea = raw_input()
longitud = len(linea)
i = 0
while i < longitud:
    numero = ''
    if linea[i].isalpha():
        print(linea[i], end='')
        i += 1
    else:
        while linea[i].isdigit():
            numero += linea[i]
            i += 1
        numero = long(numero, 2)
        print(numero % 1000000007, end='')
