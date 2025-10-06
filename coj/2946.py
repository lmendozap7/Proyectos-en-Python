casos = int(raw_input())
for i in range(casos):
    numero = int(raw_input())
    if numero % 2 != 0:
        numero *= 2
    else:
        while numero % 2 == 0:
            numero /= 2
    print numero
