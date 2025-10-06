while True:
    cadena=[]
    numero=int(raw_input())
    if numero<0:
        break
    while numero>0:
        ternario=numero%3
        numero/=3
        cadena.append(str(ternario))
    print(''.join(reversed(cadena)))