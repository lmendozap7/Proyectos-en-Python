primos = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
casos = int(raw_input())
for i in range(casos):
    numero = int(raw_input())
    primorial = 1
    for primo in primos:
        if numero >= primo:
            primorial *= primo
        else:
            break
    print primorial
