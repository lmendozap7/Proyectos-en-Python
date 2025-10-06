grande = map(int, raw_input().split('.'))
chiquita = map(int, raw_input().split('.'))
mayor, menor = '', ''
for i in range(4):
    mayor += bin(grande[i])[2:].zfill(8)
    menor += bin(chiquita[i])[2:].zfill(8)
print int(mayor, 2) - int(menor, 2) + 1
