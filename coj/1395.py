import math
casos=int(raw_input())
for i in range(casos):
    numero=int(raw_input())
    if numero==0 or numero==1:
        print '1'
    else:
        print int((0.5 * math.log10(2 * numero * math.pi) + numero * math.log10(numero / math.e) + 1))