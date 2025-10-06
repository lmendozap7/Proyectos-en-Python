def convertirNumero(cadena):
    numero = cadena[:2] + int(cadena[3]) * '0'
    return int(numero)


while True:
    cadena = raw_input()
    if cadena == '00e0':
        break
    else:
        numero = convertirNumero(cadena)
        arreglo = numero * [0]
        elQueToca = -1
        contadorDeDos = 0
        while arreglo.count(1) != numero - 1:
            if arreglo[(elQueToca + 1) % numero] == 0:
                contadorDeDos += 1
                elQueToca = (elQueToca + 1) % numero
                if contadorDeDos == 2:
                    contadorDeDos = 0
                    arreglo[elQueToca] = 1
            else:
                elQueToca = (elQueToca + 1) % numero
        print arreglo.index(0) + 1
