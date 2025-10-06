while True:
    casos = int(raw_input())
    if casos == 0:
        break
    mayor = 0
    for i in range(casos):
        base, exponente = map(long, raw_input().split())
        calculo = base ** exponente
        if calculo > mayor:
            mayor = calculo
            guardarBase, guardarExp = base, exponente
    print guardarBase, guardarExp