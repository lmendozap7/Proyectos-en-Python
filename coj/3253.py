casos = int(raw_input())
conjunto = set()
for i in range(casos):
    numeros = raw_input().split()
    del numeros[0]
    for numero in numeros:
        conjunto.add(numero)
print(len(conjunto))
