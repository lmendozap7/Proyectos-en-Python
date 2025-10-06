from __future__ import print_function

bandera = False
for i in range(1, 6):
    if 'FBI' in raw_input():
        print(i, end=' ')
        bandera = True
if not bandera:
    print('HE GOT AWAY!')
