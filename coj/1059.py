while (True):
    contador = 0
    numero = int(raw_input())
    if numero == 0:
        break
    binario = bin(numero)
    contador += binario.count('1')
    print("The parity of " + str(binario[2:]) + " is " + str(contador) + " (mod 2).")