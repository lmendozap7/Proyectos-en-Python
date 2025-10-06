for i in range(int(raw_input())):
    direcciones = raw_input().split()
    dirA = map(int, direcciones[0].split('.'))
    dirB = map(int, direcciones[1].split('.'))
    dirC = map(int, direcciones[2].split('.'))
    listaA = []
    listaB = []
    listaC = []
    for j in range(4):
        listaA.append(chr(dirA[j]))
        listaB.append(chr(dirB[j]))
        listaC.append(chr(dirC[j]))
    listaA = ''.join(listaA)
    listaB = ''.join(listaB)
    listaC = ''.join(listaC)
    if listaA <= listaC <= listaB:
        print 'YES'
    else:
        print 'NO'
