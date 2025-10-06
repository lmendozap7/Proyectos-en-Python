numero = int(raw_input())
contador = 0
while (numero != 0):
    lista = list(str(numero))
    lista.sort()
    ordenado = int(''.join(lista))
    numero = numero - ordenado
    contador += 1
print contador
