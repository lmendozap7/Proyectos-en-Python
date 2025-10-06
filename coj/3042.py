raw_input()
lista = [int(i) for i in raw_input().split()]
lista.sort()
contador = 0
while lista:
    if lista[-1] >= len(lista):
        lista.pop()
        contador += 1
    else:
        lista = [elemento - 1 for elemento in lista if elemento != 1]
        contador += 1
print contador
