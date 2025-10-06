from math import sqrt

suma = 1
for i in range(int(raw_input())):
    suma = 1
    numero = int(raw_input())
    if numero == 1:
        print(0)
    else:
        raiz = sqrt(numero)
        for j in range(2, int(raiz + 1)):
            if numero % j == 0:
                if j == raiz:
                    suma += j
                else:
                    suma += j + numero / j
        print(suma)