try:
    while True:
        a, b = map(int, raw_input().split())
        print 2 * a * b
except EOFError:
    exit()
