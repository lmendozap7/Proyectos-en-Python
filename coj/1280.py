while True:
    numero = int(raw_input())
    if numero == 0:
        break
    print(str(numero) + ' => ' + str(numero * numero - (numero - 1)))
