while True:
    cantidad = raw_input()
    if cantidad == '-1':
        break
    suma = 0
    contador = 0
    lista = [int(x) for x in raw_input().split()]
    for i in lista:
        suma += i
        if suma % 100 == 0:
            contador += 1
    print contador