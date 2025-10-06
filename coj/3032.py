t, a, b = [int(i) for i in raw_input().split()]
solucion = (t ** a - 1) / (t ** b - 1)
print solucion, len(str(solucion))
