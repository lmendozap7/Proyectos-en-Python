while True:
    numero = raw_input()
    if numero == '0':
        break
    else:
        sumaOriginal = 0
        for numerito in numero:
            sumaOriginal += int(numerito)
        if sumaOriginal % 9 == 0:
            contador = 1
            while sumaOriginal != 9:
                contador += 1
                sumaSecundaria = 0
                for digito in str(sumaOriginal):
                    sumaSecundaria += int(digito)
                sumaOriginal = sumaSecundaria
            print str(numero) + ' is a multiple of 9 and has 9-degree ' + str(contador) + '.'
        else:
            print str(numero) + ' is not a multiple of 9.'
