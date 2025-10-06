suma = 0
raw_input()
lista = map(int, raw_input().split())
lista.sort()
for i in range(len(lista) / 2 + 1):
    if lista[1] % 2 == 0:
        suma += lista[i] / 2 + 1
    else:
        suma += (lista[i] + 1) / 2
print(suma)