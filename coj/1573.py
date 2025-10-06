for i in range(int(raw_input())):
    numero = long(raw_input(), 16)
    acumulado = numero * (numero + 1) / 2
    if acumulado % numero == 0:
        print 'YES'
    else:
        print 'NO'
