n = int(input())

num_list = list(map(int, input().split()))

max_result = num_list[0]
dp_list = [0] * 100000
dp_list[0] = num_list[0]
for i in range(1, n):
    dp_list[i] = max(num_list[i], dp_list[i-1] + num_list[i])  # 새출발 vs 지금까지의합
    max_result = max(dp_list[i], max_result)

print(max_result)