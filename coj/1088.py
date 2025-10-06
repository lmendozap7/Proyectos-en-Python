try:
    while True:
        lista = [float(i) for i in raw_input().split()][1:]
        contador = 0
        while lista:
            primero = lista[0]
            del lista[0]
            while lista and lista[0] - primero <= 1:
                del lista[0]
            contador += 1
        print contador
except EOFError:
    exit()
