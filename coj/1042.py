casos = int(raw_input())
promedio = 0
for i in range(casos):
    hipotenusa, cateto = map(float, raw_input().split())
    cateto2 = (hipotenusa ** 2 - cateto ** 2) / (2 * hipotenusa)
    promedio += cateto2
    print("%.1f" % cateto2)
print("%.1f" % (promedio / casos))