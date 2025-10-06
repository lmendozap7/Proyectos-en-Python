conjunto = set()
for i in range(10):
    conjunto.add(int(raw_input()) % 42)
print(len(conjunto))