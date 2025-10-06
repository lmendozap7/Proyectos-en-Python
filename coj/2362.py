casos = int(raw_input())
for i in range(casos):
    cantidad = int(raw_input())
    if cantidad == 1:
        print 1
    else:
        suma = 1
        for j in range(1, cantidad):
            suma += 4 * j
        print suma
