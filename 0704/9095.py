t = int(input())
sum_list = [0]*11
sum_list[1] = 1
sum_list[2] = 2
sum_list[3] = 4

for i in range(4, 11):
    sum_list[i] = sum_list[i-1] + sum_list[i-2] + sum_list[i-3]
for _ in range(t):
    n = int(input())
    print(sum_list[n])