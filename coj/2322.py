casos = int(raw_input())
for i in range(casos):
    lista = map(int, raw_input().split())
    suma = 0
    for j in lista[1:]:
        suma += j - 1
    print(suma + 1)