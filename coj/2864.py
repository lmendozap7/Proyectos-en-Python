for i in range(int(raw_input())):
    linea=raw_input().split()
    ip1 = map(int, linea[0].split('.'))
    ip2 = map(int, linea[1].split('.'))
    ip3 = map(int, linea[2].split('.'))
    a = ip1[0] * 16777216 + ip1[1] * 65536 + ip1[2] * 256 + ip1[3]
    b = ip2[0] * 16777216 + ip2[1] * 65536 + ip2[2] * 256 + ip2[3]
    c = ip3[0] * 16777216 + ip3[1] * 65536 + ip3[2] * 256 + ip3[3]
    if min(a, b) <= c <= max(a, b):
        print 'YES'
    else:
        print 'NO'
