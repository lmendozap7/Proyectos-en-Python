try:
    while True:
        arreglo = raw_input().split()
        larga = arreglo[0]
        corta = arreglo[1]
        while larga.__contains__(corta):
           larga= larga.replace(corta, '')
        print larga
except EOFError:
    exit()
