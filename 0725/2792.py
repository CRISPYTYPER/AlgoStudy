import sys
from math import ceil
input = sys.stdin.readline

n, m = map(int, input().split())
list = [0] # i번 색상의 보석 수 집어넣음. 1번 array부터 집어넣기
for i in range(m):
    list.append(int(input()))
max_gem = max(list)
st, en = 1, max_gem
min_jealous = 300001
while(st <= en):
    mid = (st+en)//2
    student_temp = 0
    for i in range(1, m+1):
        student_temp += ceil(list[i]/mid)
    if(n >= student_temp):
        en = mid - 1
        min_jealous = mid
    elif (n < student_temp):
        st = mid + 1

print(min_jealous)