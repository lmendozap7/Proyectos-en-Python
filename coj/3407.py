casos = int(raw_input())
annos, mujeres = [], []
for i in range(casos):
    anno, mujer = map(int, raw_input().split())
    annos.append(anno)
    mujeres.append(mujer)
casos -= 2
promedio = (mujeres[0] + mujeres[1] + mujeres[2]) / 3
salida = str(annos[0]) + ' ' + str(annos[1]) + ' ' + str(annos[2])
for j in range(casos):
    anno1 = annos[j]
    anno2 = annos[j + 1]
    anno3 = annos[j + 2]
    mujer1 = mujeres[j]
    mujer2 = mujeres[j + 1]
    mujer3 = mujeres[j + 2]
    media = (mujer1 + mujer2 + mujer3) / 3
    if media <= promedio:
        promedio = media
        salida = str(anno1) + ' ' + str(anno2) + ' ' + str(anno3)
print(salida)
