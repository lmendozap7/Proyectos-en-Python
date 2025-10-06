casos = int(raw_input())
for i in range(casos):
    arreglo = []
    suma = 0
    balas, trabajos = map(int, raw_input().split())
    for j in range(trabajos):
        arreglo.append(int(raw_input().split()[0]))
    arreglo.sort(reverse=True)
    for j in range(balas):
        suma += arreglo[j]
    print(suma)
