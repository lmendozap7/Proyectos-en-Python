cantidad=int(raw_input())
lista=[]
for i in range(cantidad):
    lista.append(int(raw_input()))
lista.sort()
for i in lista:
    print i
