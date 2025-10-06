def total_bolas(pisos):
    bolas = 0
    for i in range(1, pisos + 1):
        bolas += i ** 2
    return bolas


while True:
    numero = int(raw_input())
    if numero == 0:
        break
    else:
        print(total_bolas(numero))