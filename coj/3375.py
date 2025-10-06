casos = int(raw_input())
for i in range(casos):
    contador = 0
    primera, segunda = raw_input().split()
    for i in range(len(primera)):
        if primera[i] != segunda[i]:
            contador += 1
    print contador