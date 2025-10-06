try:
    while True:
        numero = long(raw_input())
        if numero == 1:
            print(1)
        else:
            print(numero * 2 - 2)
except:
    exit()