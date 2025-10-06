primero, segundo = map(str, raw_input().split())
contador = 0
for i in primero:
    for j in segundo:
        contador += int(i) * int(j)
print contador