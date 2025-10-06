import math

MOD = 1000000
MAXV = 1000001
x = [0] * MAXV
x[0]=1
for i in range(1, MAXV):
    x[i] = (x[int(i - math.sqrt(i))] + x[int(math.log(i))] + x[int(i * math.sin(i)**2)]) % MOD
N = int(raw_input())
while N != -1:
    print x[N]
    N = int(raw_input())
