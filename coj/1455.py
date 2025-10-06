import fractions

contador = 0
n, a, b = map(long, raw_input().split())
for i in range(a, b):
    if fractions.gcd(i, n) == 1:
        contador += 1
print contador
