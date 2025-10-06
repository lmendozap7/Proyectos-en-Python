raw_input()
letras = []
numeros = map(int, raw_input().split())
numeros.sort()
sumatoria = sum(numeros)
for numero in numeros:
    if numero % 2 == 0:
        letras.append('P')
    else:
        letras.append('I')
if letras.count('P') == len(letras):
    print(-1)
elif sumatoria % 2 != 0:
    print(sumatoria)
else:
    valor = numeros[letras.index('I')]
    print(sumatoria - valor)