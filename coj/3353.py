cantidad = int(raw_input().split()[1])
objetos = [int(i) for i in raw_input().split()]
objetos.sort()
contador = 0
for i in range(cantidad):
    if objetos[i] < 0:
        contador += objetos[i]
    else:
        break
print abs(contador)
