from bisect import bisect_right

m = [int(bin(i).replace("0b", "")) for i in range(1, 513)]
for i in range(int(raw_input())):
    print bisect_right(m, int(raw_input()))
