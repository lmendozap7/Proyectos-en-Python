for i in range(int(raw_input())):
    contador = 0
    longitud = int(raw_input())
    arreglo = [False] * longitud
    for j in range(2, longitud + 1):
        for k in range(j - 1, longitud, j):
            arreglo[k] = not arreglo[k]
    for j in range(longitud):
        if not arreglo[j]:
            contador += 1
    print(contador)