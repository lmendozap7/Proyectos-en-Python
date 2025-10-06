from math import factorial

for i in range(int(raw_input())):
    numero = int(raw_input())
    sumatoria = 0
    for j in range(numero):
        sumatoria += factorial(numero) / factorial(numero - j)
    print sumatoria % 1000003
