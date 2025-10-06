for i in range(int(raw_input())):
    lista = [int(numero) for numero in raw_input().split()][1:]
    longitud = len(lista)
    bandera = False
    for j in range(longitud):
        for k in range(j + 1, longitud+1):
            if sum(lista[j:k]) == 0:
                bandera = True
                break
    if bandera:
        print 'YES'
    else:
        print 'NO'
