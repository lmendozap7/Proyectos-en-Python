try:
    while True:
        lista = map(int, raw_input().split())
        cont1 = 0
        a = min(lista)
        b = max(lista)
        for i in range(a, b + 1):
            cont = 0
            temp = i
            while temp != 1:
                if temp % 2 == 0:
                    temp /= 2
                else:
                    temp = temp * 3 + 1
                cont += 1
            if cont1 < cont + 1:
                cont1 = cont + 1
        print lista[0], lista[1], cont1
except EOFError:
    exit()