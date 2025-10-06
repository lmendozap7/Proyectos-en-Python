casos = int(raw_input())
for i in range(casos):
    b = 0
    r = 0
    o = 0
    k = 0
    e = 0
    n = 0
    contrasena = raw_input()
    for letra in contrasena:
        if letra == 'B':
            b += 1
        elif letra == 'R':
            r += 1
        elif letra == 'O':
            o += 1
        elif letra == 'K':
            k += 1
        elif letra == 'E':
            e += 1
        elif letra == 'N':
            n += 1
    if b == r == o == k == e == n:
        print('No Secure')
    else:
        print('Secure')
