lista = []
for i in range(int(raw_input())):
    a, b, c = map(int, raw_input().split())
    if a < b + c and b < a + c and c < a + b:
        lista.append(a + b + c)
print(min(lista))