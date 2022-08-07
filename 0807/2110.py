import sys

input = sys.stdin.readline

N, C = map(int, input().split())
house_list = sorted(list(int(input()) for _ in range(N))) # 집들의 좌표 리스트
# 두 공유기 사이 가능한 최소 거리를 기준으로 이분탐색 하면 될듯

st = 1
en = max(house_list) - min(house_list)
result = []
while st <= en:
    mid = (st + en) // 2
    wifi_cnt = 1 # 맨 왼쪽집에는 무조건 와이파이 설치
    left_wifi = house_list[0]
    for house in house_list:
        if left_wifi + mid <= house:
            wifi_cnt += 1
            left_wifi = house
    if wifi_cnt >= C:
        st = mid + 1
        result.append(mid)
    else:
        en = mid - 1


print(max(result))