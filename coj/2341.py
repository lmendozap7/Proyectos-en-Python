calculos, respuestas = map(int, raw_input().split())
almacen = []
for i in range(calculos):
    almacen.append(raw_input())
for j in range(respuestas):
    resultado = raw_input()
    if ' ' not in resultado:
        print 'not found'
    else:
        if resultado in almacen:
            print 'ok'
        else:
            print 'wrong'
