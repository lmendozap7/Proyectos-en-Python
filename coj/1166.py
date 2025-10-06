casos = int(raw_input())
for i in range(casos):
    pares = 0
    impares = 0
    raw_input()
    lista = raw_input().split()
    for j in lista:
        if int(j) % 2 == 0:
            pares += 1
        else:
            impares += 1
    print '%d even and %d odd.' %(pares,impares)