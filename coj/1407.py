from decimal import Decimal

num2 = Decimal(2)
for i in range(10):
    total = Decimal(raw_input())
    tiene_mas = Decimal(raw_input())
    calculo = (total - tiene_mas) / num2
    print(calculo + tiene_mas)
    print(calculo)