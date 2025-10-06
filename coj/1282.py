from datetime import date

while True:
    cantidad = int(raw_input())
    if cantidad == 0:
        break
    fechas = []
    consumos = []
    contadorFechas = 0
    contadorConsumo = 0
    for i in range(cantidad):
        linea = map(int, raw_input().split())
        fechas.append(date(linea[2], linea[1], linea[0]))
        consumos.append(linea[3])
    cantidad -= 1
    for i in range(cantidad):
        if (fechas[i + 1] - fechas[i]).days == 1:
            contadorFechas += 1
            contadorConsumo += consumos[i + 1] - consumos[i]
    print contadorFechas, contadorConsumo
