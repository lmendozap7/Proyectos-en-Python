from math import log

while True:
    numero = int(raw_input())
    if numero == 0:
        break
    else:
        base = 2
        while True:
            logaritmo = log(numero, base)
            if logaritmo == int(logaritmo):
                break
            else:
                base += 1
    print int(logaritmo) if base != numero else 1
