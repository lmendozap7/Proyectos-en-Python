from datetime import date

fecha1 = raw_input().split(':')
fecha2 = raw_input().split(':')
calendario1 = date(int(fecha1[0]), int(fecha1[1]), int(fecha1[2]))
calendario2 = date(int(fecha2[0]), int(fecha2[1]), int(fecha2[2]))
print abs(calendario1 - calendario2).days
