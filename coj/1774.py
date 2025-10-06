palabra = raw_input()
if palabra.istitle() or palabra.islower():
    print(palabra)
else:
    print(palabra.swapcase())