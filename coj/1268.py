from math import factorial

numero = int(raw_input())
if factorial(numero) % (numero * numero) == 0:
    print 'YES'
else:
    print 'NO'
