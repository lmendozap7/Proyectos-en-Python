arreglo = ["Airborne", "Pagfloyd"]
casos = int(raw_input())
for i in range(casos):
    a, b = map(int, raw_input().split())
    print arreglo[b] + " wins."