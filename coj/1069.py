for i in range(int(raw_input())):
    linea = map(int,raw_input().split())
    bot = linea[0] + linea[1]
    botC = linea[2]
    if botC == 0 or botC == 1:
        print(0)
    else:
        cantIni = 0
        while bot / botC >= 1:
            cantIni += bot / botC
            bot = bot / botC + bot % botC
        print(cantIni)