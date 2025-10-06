while True:
    numero = long(raw_input())
    if numero == 0:
        break
    if numero % 11 == 0:
        print numero, 'is a multiple of 11.'
    else:
        print numero, 'is not a multiple of 11.'
