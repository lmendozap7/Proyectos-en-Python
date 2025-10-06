casos = int(raw_input())
for i in range(casos):
    numero = long(raw_input())
    cadena = raw_input()
    restante = numero % len(cadena)
    if numero == 0:
        print(cadena)
    else:
        print(cadena[len(cadena) - restante:] + cadena[0:len(cadena) - restante])
