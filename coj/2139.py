try:
    while True:
        cadena = raw_input().split()
        chiquita = list(cadena[0])
        grande = list(cadena[1])
        while len(chiquita) > 0:
            if chiquita[0] in grande:
                del grande[0:grande.index(chiquita[0]) + 1]
                del chiquita[0]
            else:
                print 'No'
                break
        if len(chiquita) == 0:
            print 'Yes'
except EOFError:
    exit()
