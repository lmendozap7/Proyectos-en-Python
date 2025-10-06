lista = []
mayor = 1
for i in range(int(raw_input())):
    arreglo = raw_input().split()
    arreglo.sort()
    lista.append(arreglo)
    for i in lista:
        mayor = max(mayor, lista.count(i))
print(mayor)