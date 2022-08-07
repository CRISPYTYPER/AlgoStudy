import sys
input = sys.stdin.readline

N, M = map(int, input().split())
times_list = [int(input()) for _ in range(N)]

st = min(times_list)
en = M * min(times_list)
result = 0

while(st<=en):
    mid = (st+en) // 2
    possible_people = 0
    for time in times_list:
        possible_people += mid // time # 한 심사대에서 주어진 시간동안 몇명 심사할 수 있는지
    if possible_people >= M:
        en = mid - 1
        result = mid
    else:
        st = mid + 1
print(result)