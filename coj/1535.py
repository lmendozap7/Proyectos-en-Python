print "Lumberjacks:"
casos = int(raw_input())
for i in range(casos):
    arreglo = map(int, raw_input().split())
    derecho = sorted(arreglo)
    izquierdo = sorted(arreglo, reverse=True)
    if arreglo == derecho or arreglo == izquierdo:
        print 'Ordered'
    else:
        print 'Unordered'