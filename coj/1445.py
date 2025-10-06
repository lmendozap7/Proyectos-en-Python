while True:
    num1, num2, num3 = map(int, raw_input().split())
    if num1 == num2 == num3 == 0:
        break
    if num3 - num2 == num2 - num1:
        print "AP", (num3 * 2 - num2)
    else:
        print "GP", num3 ** 2 / num2