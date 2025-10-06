centavos = (5, 10, 25, 50)
MAXV = 7490
monedas = [0] * MAXV
for i in range(MAXV):
    monedas[i] = 1
for i in range(4):
    for j in range(centavos[i], MAXV):
        monedas[j] += monedas[j - centavos[i]]
try:
    while True:
        print(monedas[int(raw_input())])
except EOFError:
    exit()