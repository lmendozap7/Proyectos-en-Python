while True:
    linea = raw_input()
    if linea == '0 0':
        break
    a, b = map(int, linea.split())
    diferencia = b - a
    print a - diferencia
