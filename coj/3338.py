from __future__ import print_function

casos = int(raw_input())
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(casos):
    mensaje = raw_input()
    codigo = raw_input()
    print (i+1, end="")
    print (" ", end="")
    for j in range(len(mensaje)):
        if mensaje[j] in alfabeto:
            print(codigo[alfabeto.index(mensaje[j])], end="")
        else:
            print(mensaje[j], end="")
    print()
