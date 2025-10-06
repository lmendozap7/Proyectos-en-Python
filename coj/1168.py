from string import ascii_uppercase

alfabeto = ascii_uppercase
codigo = [''] * 26
linea = raw_input()
numero = int(raw_input()) - 1
paraDecodificar = raw_input()
for letra in linea:
    if numero == 0:
        codigo[0] = letra
    else:
        codigo[numero % 26] = letra
    numero += 1
for letra in alfabeto:
    if letra not in codigo:
        if numero == 0:
            codigo[0] = letra
        else:
            codigo[numero % 26] = letra
        numero += 1
salida = []
for letra in paraDecodificar:
    salida.append(alfabeto[codigo.index(letra)])
print ''.join(salida)
