from __future__ import print_function
import math


for i in range(int(raw_input())):
    radio, lados = map(float, raw_input().split())
    angCentral = 360 / lados
    lado = 2 * radio * math.sin(math.radians(angCentral / 2))
    lado2 = 2 * radio * math.tan(math.radians(angCentral / 2))
    print("%.4f %.4f" % (lado * lados, lado2 * lados))