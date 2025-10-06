arreglo = []
cantidad = 0
for i in range(8):
    arreglo.append(int(raw_input()))
cantidad = max((arreglo[0] + arreglo[1] + arreglo[2] + arreglo[3]), cantidad)
cantidad = max((arreglo[1] + arreglo[2] + arreglo[3] + arreglo[4]), cantidad)
cantidad = max((arreglo[2] + arreglo[3] + arreglo[4] + arreglo[5]), cantidad)
cantidad = max((arreglo[3] + arreglo[4] + arreglo[5] + arreglo[6]), cantidad)
cantidad = max((arreglo[4] + arreglo[5] + arreglo[6] + arreglo[7]), cantidad)
cantidad = max((arreglo[5] + arreglo[6] + arreglo[7] + arreglo[0]), cantidad)
cantidad = max((arreglo[6] + arreglo[7] + arreglo[0] + arreglo[1]), cantidad)
cantidad = max((arreglo[7] + arreglo[0] + arreglo[1] + arreglo[2]), cantidad)
print(cantidad)
