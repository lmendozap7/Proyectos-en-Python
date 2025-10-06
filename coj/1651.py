raw_input()
lista = map(int, raw_input().split())
consultas = int(raw_input())
for i in range(consultas):
    linea = raw_input().split()
    a = int(linea[0])
    b = int(linea[1])
    print min(lista[a-1:b])
