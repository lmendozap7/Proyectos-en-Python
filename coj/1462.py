cantidad = int(raw_input())
suma, numero = 0, 0
for i in range(cantidad):
    numero = long(raw_input())
    suma = numero % 128 + suma % 128
    print suma % 128