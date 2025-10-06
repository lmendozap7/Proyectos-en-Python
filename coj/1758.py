mayor, menor = 0, 0
for i in range(int(raw_input())):
    numero = int(raw_input())
    if numero > 0 and numero > mayor:
        mayor = numero
    if numero < 0 and numero < menor:
        menor = numero
print mayor + abs(menor)
