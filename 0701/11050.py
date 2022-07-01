n, k = map(int, input().split())

if(k > n-k): # n C r = n C n-r
    k = n-k

# binom_list = [[0] * (k+1) for _ in range(n+1)] # 0행은 취급 안함. 왜냐하면 0C1 취급 안함
# 위처럼 하면 런타임 에러났음. 0 1 입력하면 binom_list가 [1][1]번째 메모리가 안만들어짐
binom_list = [[0] * (1001) for _ in range(1001)]
# print(binom_list)
for i in range(1, n+1):
    binom_list[i][0] = 1
binom_list[1][1] = 1
for i in range(2, n+1):
    for j in range(1, k+1):
        binom_list[i][j] = (binom_list[i-1][j-1] + binom_list[i-1][j]) % 10007

print(binom_list[n][k])