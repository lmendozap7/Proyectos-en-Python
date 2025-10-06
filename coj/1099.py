while True:
      cadena=raw_input()
      if cadena=='0':
         break
      arreglo=sorted(map(int,cadena.split()))
      if arreglo[0]**2+arreglo[1]**2==arreglo[2]**2:
         print 'right'
      else:
           print 'wrong'