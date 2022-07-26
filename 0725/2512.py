import sys
input = sys.stdin.readline

n = int(input())
city_list = [0] + list(map(int, input().split())) # 1번 인덱스부터 사용
m = int(input())

# 상한액을 변수로 잡으면 될듯
st, en = 1, max(city_list)
max_money = 0
while(st<=en):
    mid = (st + en) // 2
    money_sum = 0
    for i in range(1, n + 1):
        if city_list[i] > mid: # 요구 예산이 상한액보다 크면
            money_sum += mid
        else: # 상한액 이하면
            money_sum += city_list[i]
    if money_sum > m: # 다 더해본 예산이 국가의 예산보다 많으면(상한액을 줄여야함)
        en = mid - 1
    elif money_sum < m: # 예산이 남아 돌면 (상한액 올려도 됨)
        st = mid + 1
        max_money = mid
    else:
        st = mid + 1
        max_money = mid
print(max_money)
