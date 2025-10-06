casos = int(raw_input())
lista = [0] * 2015
for i in range(casos):
    a, b = map(int, raw_input().split())
    lista[a] += b
for i in range(2015):
    if lista[i] != 0:
        print i, lista[i]
