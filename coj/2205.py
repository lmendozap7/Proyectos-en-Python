contador = 0
a, b = map(int, raw_input().split())
for i in range(a, b + 1):
    contador += bin(i).count('1')
print(contador)