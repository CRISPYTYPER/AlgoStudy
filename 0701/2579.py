n = int(input())

stair_list = [0] * (n+1)
for i in range(n):
    stair_list[i+1] = int(input())

for i in range(2, n+1):
    stair_list[i] += max(stair_list[i-2], stair_list[i-1])

