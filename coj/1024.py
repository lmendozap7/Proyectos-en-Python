while True:
    longitud = float(raw_input())
    if longitud == 0:
        break
    contador = 0
    sumatoria = 0.0
    sumar = 2.0
    while sumatoria < longitud:
        contador += 1
        sumatoria += 1 / sumar
        sumar += 1
    print contador, "card(s)"
