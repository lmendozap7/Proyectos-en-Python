for i in range(int(raw_input())):
    x, y = map(int, raw_input().split())
    if x == y or x - y == 2:
        if x % 2 != 0:
            print(x + y - 1)
        else:
            print(x + y)
    else:
        print("No Number")