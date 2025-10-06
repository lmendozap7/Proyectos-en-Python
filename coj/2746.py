palabra = raw_input()
vocales = 'AEIOU'
contar_vocales = 0
for letra in palabra:
    if letra in vocales:
        contar_vocales += 1
print contar_vocales, len(palabra) - contar_vocales