primero, segundo, tercero = [int(i) + 1 for i in raw_input().split()]
frecuencias = [0] * 16005
for i in range(1, primero):
    for j in range(1, segundo):
        for k in range(1, tercero):
            frecuencias[i + j + k] += 1
print frecuencias.index(max(frecuencias))
