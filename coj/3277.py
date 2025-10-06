cantidad = int(raw_input())
semillas = map(int, raw_input().split())
semillas.sort()
bandera = False
intervalo = semillas[1] - semillas[0]
for i in range(cantidad - 1):
    if semillas[i + 1] - semillas[i] != intervalo:
        bandera = True
        break
if bandera:
    print("NO")
else:
    print("YES")
