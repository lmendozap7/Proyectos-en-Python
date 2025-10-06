for i in range(int(raw_input())):
    suma = 0
    raw_input()
    cantidad = int(raw_input())
    for j in range(cantidad):
        suma += long(raw_input())
    if suma % cantidad == 0:
        print('YES')
    else:
        print('NO')