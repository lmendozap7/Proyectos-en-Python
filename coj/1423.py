from math import sqrt

try:
    while True:
        numero = float(raw_input())
        print "%.6f" % sqrt(pow(numero / 2, 2) - pow(numero / 4, 2))
except EOFError:
    exit()