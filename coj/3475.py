import math

a, b = map(int, raw_input().split())
print a * b * math.pow(math.sin(a), 2) + a * b * pow(math.cos(a), 2)
