import sys
from math import floor
input = sys.stdin.readline

k, n = map(int, input().split())
lines = [0] # 1번 인덱스부터 집어넣음
for i in range(k):
    lines.append(int(input()))

st, en = 1, max(lines) # 랜선 길이가 변수
max_line = -1
while(st<=en):
    line_cnt = 0
    mid = (st+en)//2
    for i in range(k):
        line_cnt += floor(lines[i+1]/mid)
    if n < line_cnt: #원하는 개수보다 더 많이 만들어지면(이것보다 더 길게 만들 수도 있다는 뜻)
        st = mid + 1
        max_line = mid
    elif n > line_cnt: #원하는 개수보다 더 적게 만들어지면(자르는 길이를 더 줄여야됨)
        en = mid - 1
    else:
        st = mid + 1
        max_line = mid
print(max_line)