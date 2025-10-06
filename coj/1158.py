for i in range(int(raw_input())):
    cadena = bin(long(raw_input()))
    print(2 ** (len(cadena) - 1 - cadena.rfind('1')))