while True:
    numero1, numero2 = raw_input().split()
    if numero1 == numero2 == '*':
        break
    num1, num2 = long(numero1, 17), long(numero2, 17)
    if num1 < num2:
        print('<')
    elif num1 > num2:
        print('>')
    else:
        print('=')