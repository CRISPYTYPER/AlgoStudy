n = int(input())

rgb_list = [[0] * 3 for _ in range(n + 1)]

for i in range(1, n + 1):
    rgb_list[i][0], rgb_list[i][1], rgb_list[i][2] = map(int, input().split())

for i in range(2, n + 1):
    rgb_list[i][0] = min(rgb_list[i - 1][1], rgb_list[i - 1][2]) + rgb_list[i][0]
    rgb_list[i][1] = min(rgb_list[i - 1][0], rgb_list[i - 1][2]) + rgb_list[i][1]
    rgb_list[i][2] = min(rgb_list[i - 1][0], rgb_list[i - 1][1]) + rgb_list[i][2]

print(min(rgb_list[n][0], rgb_list[n][1], rgb_list[n][2]))

# 머릿속에서 안떠올랐음