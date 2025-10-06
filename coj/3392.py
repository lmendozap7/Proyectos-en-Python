while True:
    numero = long(raw_input())
    if numero == 0:
        break
    elif numero == 1 or numero == 2:
        print '0'
    else:
        print numero * 4
