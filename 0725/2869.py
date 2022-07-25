import math
a, b, v = map(int, input().split())

if a>=v:
    print(1)
else:
    day = 1
    day += math.ceil((v-a)/(a-b))
    print(day)