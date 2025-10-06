from __future__ import print_function

numero0 = ('+---+', '|   |', '|   |', '+   +', '|   |', '|   |', '+---+')
numero1 = ('    +', '    |', '    |', '    +', '    |', '    |', '    +')
numero2 = ('+---+', '    |', '    |', '+---+', '|    ', '|    ', '+---+')
numero3 = ('+---+', '    |', '    |', '+---+', '    |', '    |', '+---+')
numero4 = ('+   +', '|   |', '|   |', '+---+', '    |', '    |', '    +')
numero5 = ('+---+', '|    ', '|    ', '+---+', '    |', '    |', '+---+')
numero6 = ('+---+', '|    ', '|    ', '+---+', '|   |', '|   |', '+---+')
numero7 = ('+---+', '    |', '    |', '    +', '    |', '    |', '    +')
numero8 = ('+---+', '|   |', '|   |', '+---+', '|   |', '|   |', '+---+')
numero9 = ('+---+', '|   |', '|   |', '+---+', '    |', '    |', '+---+')
espacio = ('     ', '     ', '  o  ', '     ', '  o  ', '     ', '     ')
diccionario = {'0': numero0, '1': numero1, '2': numero2, '3': numero3, '4': numero4, '5': numero5, '6': numero6,
               '7': numero7, '8': numero8, '9': numero9}
while True:
    linea = raw_input()
    if linea == 'end':
        print(linea)
        break
    primero, segundo, tercero, cuarto = diccionario[linea[0]], diccionario[linea[1]], diccionario[linea[3]], \
                                        diccionario[linea[4]]
    for i in range(7):
        print(primero[i] + '  ' + segundo[i] + espacio[i] + tercero[i] + '  ' + cuarto[i])
    print()
    print()
