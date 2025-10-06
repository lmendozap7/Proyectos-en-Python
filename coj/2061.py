for i in range(int(raw_input())):
    x, n = map(int, raw_input().split())
    sumatoria = 1
    for j in range(1, n + 1):
        sumatoria += pow(x, j, 1000000007)
    print(sumatoria % 1000000007)