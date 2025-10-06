numero=int(raw_input())
if numero==0:
   print '1'
elif numero>0:
     print numero*(numero+1)/2
else:
     print -1 * (numero * (numero - 1) / 2) + 1