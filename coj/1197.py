ip1 = map(int, raw_input().split('.'))
ip2 = map(int, raw_input().split('.'))
mayor = ip1[0] * 16777216 + ip1[1] * 65536 + ip1[2] * 256 + ip1[3]
menor = ip2[0] * 16777216 + ip2[1] * 65536 + ip2[2] * 256 + ip2[3]
print mayor - menor + 1
