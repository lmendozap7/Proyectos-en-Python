try:
    while True:
        numero = int(raw_input())
        cuadrados = 0
        rectangulos = 0
        for i in range(1, numero + 1):
            cuadrados += i ** 2
            rectangulos += i ** 3
        print cuadrados, rectangulos
except EOFError:
    exit()