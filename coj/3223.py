def sumDedivisores(n):
    if n == 1:
        return 1
    c = n + 1
    i = 2
    while i * i < n:
        if n % i == 0:
            c += i + n / i
        i += 1
    if i * i == n:
        c += i
    return c


n = int(raw_input())
while n > 0:
    numero = int(raw_input())
    print sumDedivisores(numero)
    n -= 1
