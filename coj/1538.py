for i in range(int(raw_input())):
    print i + 1, "$" + "{:,.2f}".format(sum([float(raw_input()) for x in range(12)]) / 12.0)