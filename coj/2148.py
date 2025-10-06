casos = int(raw_input())
for i in range(casos):
    a, b, c = map(int, raw_input().split())
    discriminante = b ** 2 - 4 * a * c
    if discriminante >= 0:
        print 'SI'
    else:
        print 'NO'
