linea = raw_input().split()
cantidadMinima = int(linea[2])
diferencia = int(linea[3])
setsPorA = 0
setsPorB = 0
juegosPorA = 0
juegosPorB = 0
cadena = raw_input()
cantidadJuegos = 0
for letra in cadena:
    if letra == 'A':
        juegosPorA += 1
        cantidadJuegos += 1
    else:
        juegosPorB += 1
        cantidadJuegos += 1
    maximo = max(juegosPorA, juegosPorB)
    minimo = min(juegosPorA, juegosPorB)
    if cantidadJuegos >= cantidadMinima and maximo - minimo >= diferencia:
        if maximo == juegosPorA:
            setsPorA += 1
        else:
            setsPorB += 1
        juegosPorA = 0
        juegosPorB = 0
        cantidadJuegos = 0
print setsPorA, setsPorB
