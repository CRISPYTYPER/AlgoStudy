n = int(input())
len_list = [[0] * 1001 for _ in range(10)] # 10행 1001열 (0번째 인덱스 제외). 처음 시작하는 수를 기준으로 경우의 수를 나눔
sum_list = [0] * 1001
sum_list[1] = 10
for i in range(10):
    len_list[i][1] = 1


for i in range(2,1001):
    for j in range(10):
        for k in range(9, j-1, -1):
            len_list[j][i] += (len_list[k][i-1]) % 10007
        sum_list[i] += (len_list[j][i]) % 10007



print(sum_list[n]%10007)