try:
    while True:
        r, n = map(float, raw_input().split())
        print pow(r,n)
except EOFError:
    exit()