from __future__ import print_function

casos = int(raw_input())
for i in range(casos):
    jugadores, casillas, dados = map(int, raw_input().split())
    valoresCasillas = map(int, raw_input().split())
    valoresDados = map(int, raw_input().split())
    arregloJugadores = jugadores * [0]
    elQueLeToca = 0
    ganadores = []
    for tirada in valoresDados:
        if arregloJugadores.count(casillas - 1) != jugadores:
            arregloJugadores[elQueLeToca] += tirada
            arregloJugadores[elQueLeToca] += valoresCasillas[arregloJugadores[elQueLeToca]]
            if arregloJugadores[elQueLeToca] == casillas - 1:
                ganadores.append(str(elQueLeToca + 1))
                arregloJugadores[elQueLeToca] = 'Ya gano'
            if arregloJugadores.count('Ya gano') == jugadores:
                break
            while True:
                if arregloJugadores[(elQueLeToca + 1) % jugadores] != 'Ya gano':
                    elQueLeToca = (elQueLeToca + 1) % jugadores
                    break
                elQueLeToca = (elQueLeToca + 1) % jugadores
    if len(ganadores) == 0:
        print('-1')
    else:
        print(' '.join(ganadores))