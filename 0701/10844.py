n = int(input())

num_list = [[0] * 101 for _ in range(10)]
result = 0

for i in range(9):
    num_list[i+1][1] = 1

for i in range(9):
    num_list[i+1][2] = 2

num_list[9][2] -= 1

# 위에까지 base 설정
for i in range(3,101):
    num_list[1][i] = (num_list[1][i-2] + num_list[2][i-1]) % 1000000000
    for j in range(2, 9):
        num_list[j][i] = (num_list[j-1][i-1] + num_list[j+1][i-1]) % 1000000000
    num_list[9][i] = (num_list[8][i-1]) % 1000000000

for i in range(9):
    result += (num_list[i+1][n]) % 1000000000
print(result % 1000000000)