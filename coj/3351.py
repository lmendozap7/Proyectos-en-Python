for i in range(int(raw_input())):
    cadena = raw_input()
    alReves = ''.join(reversed(cadena))
    if cadena.isupper() and cadena.isalpha() and cadena == alReves:
        print 'YES'
    else:
        print 'NO'
