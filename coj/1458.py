x = long(raw_input(), 2)
len = 100000
first = 0
while len > 0:
    half = len / 2
    middle = first + half
    if 2 ** middle < x:
        first = middle + 1
        len -= half - 1
    else:
        len = half
print first
