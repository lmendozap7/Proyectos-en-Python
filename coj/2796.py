from fractions import Fraction

while True:
    cadena = raw_input()
    if cadena == '0':
        exit()
    cadena = cadena[:len(cadena) - 3] + cadena[len(cadena) - 4] * 3+'\t\n'
    print Fraction(cadena)