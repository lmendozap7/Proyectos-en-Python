from math import sqrt


def noEsPrimo(p):
    for x in range(2, int(sqrt(p)) + 1):
        if p % x == 0:
            return True
    return False


for i in range(int(raw_input())):
    numero = int(raw_input())+1
    salida = 1
    for primo in range(2,numero):
        if not noEsPrimo(primo):
            salida = salida * primo % 10000000000
    print salida
