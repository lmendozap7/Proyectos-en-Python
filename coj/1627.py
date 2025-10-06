potencia = []
potencia.append(5)
for i in xrange(15):
    potencia.append(potencia[i] * 5)
T = input()
while T:
    cant = i = 0
    n = input()
    while n / potencia[i]:
        cant += n / potencia[i]
        i += 1
    print cant
    T -= 1
