casos = int(raw_input())
for i in range(casos):
    sonidos = raw_input().split()
    animales = []
    while True:
        linea = raw_input()
        if linea == 'what does the fox say?':
            break
        final = linea.split()[2]
        while final in sonidos:
            sonidos.remove(final)
    print(' '.join(sonidos))
