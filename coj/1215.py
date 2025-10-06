casos = int(raw_input())
for i in range(casos):
    linea = raw_input()
    linea = linea.replace('()', '(-)')
    hora1, hora2, minuto1, minuto2, segundo1, segundo2 = 0, 0, 0, 0, 0, 0
    if linea[1] == '*':
        hora1 += 2
    if linea[4] == '*':
        hora1 += 1
    if linea[7] == '*':
        hora2 += 8
    if linea[10] == '*':
        hora2 += 4
    if linea[13] == '*':
        hora2 += 2
    if linea[16] == '*':
        hora2 += 1
    if linea[19] == '*':
        minuto1 += 4
    if linea[22] == '*':
        minuto1 += 2
    if linea[25] == '*':
        minuto1 += 1
    if linea[28] == '*':
        minuto2 += 8
    if linea[31] == '*':
        minuto2 += 4
    if linea[34] == '*':
        minuto2 += 2
    if linea[37] == '*':
        minuto2 += 1
    if linea[40] == '*':
        segundo1 += 4
    if linea[43] == '*':
        segundo1 += 2
    if linea[46] == '*':
        segundo1 += 1
    if linea[49] == '*':
        segundo2 += 8
    if linea[52] == '*':
        segundo2 += 4
    if linea[55] == '*':
        segundo2 += 2
    if linea[58] == '*':
        segundo2 += 1
    print'Case', str(i + 1) + ':', str(hora1) + str(hora2) + ':' + str(minuto1) + str(minuto2) + ':' + str(
        segundo1) + str(segundo2)