import string
from datetime import date

casos = input()
for i in range(casos):
    fecha = string.split(raw_input(), " ")
    fecha1 = fecha[0].split("-")
    fecha2 = fecha[1].split("-")
    if fecha1 == fecha2:
        print '0'
        continue
    calendario1 = date(int(fecha1[0]), int(fecha1[1]), int(fecha1[2]))
    calendario2 = date(int(fecha2[0]), int(fecha2[1]), int(fecha2[2]))
    print abs(calendario1 - calendario2).days

