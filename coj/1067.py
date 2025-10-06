listaMay = []
listaMen = []
while True:
    numero = int(raw_input())
    if numero == 0:
        break
    cadena = raw_input()
    if cadena == 'too high':
        listaMay.append(numero)
    elif cadena == 'too low':
        listaMen.append(numero)
    else:
        error = False
        for elemento in listaMay:
            if numero >= elemento:
                error = True
                break
        for elemento in listaMen:
            if numero <= elemento:
                error = True
                break
        if error:
            print("Stan is dishonest")
        else:
            print("Stan may be honest")
        listaMay = []
        listaMen = []