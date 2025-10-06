a, b, c = sorted(map(int, raw_input().split()))
orden = raw_input()
if orden == 'ABC':
    print a, b, c
elif orden == 'ACB':
    print a, c, b
elif orden == 'BAC':
    print b, a, c
elif orden == 'BCA':
    print b, c, a
elif orden == 'CAB':
    print c, a, b
else:
    print c, b, a
