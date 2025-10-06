casos = int(raw_input())
for i in range(casos):
    base, exponente = map(long, raw_input().split())
    print pow(base, exponente, 10)
