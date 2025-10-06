teclado = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"
try:
    while True:
        texto = raw_input()
        salida = []
        for i in range(len(texto)):
            if texto[i] == ' ':
                salida.append(' ')
            else:
                salida.append(teclado[teclado.index(texto[i]) - 1])
        print(''.join(salida))
except EOFError:
    exit()
