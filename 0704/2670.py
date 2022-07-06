n = int(input())

float_list = [1.0] * 10001

for i in range(1, n+1):
    float_list[i] = float(input())

dp = [1.0] * 10001
dp[1] = float_list[1]
max_result = dp[1]
for i in range(2, n+1):
    dp[i] = max(float_list[i], dp[i-1] * float_list[i])  # 새출발 할것이냐, 기존곱 * 현재 값을 할 것이냐
    # dp[i]에는 i요소까지의 경우의 수중 가장 큰 값이 담긴다
    max_result = max(dp[i],max_result)
print("%.3f" %max_result)