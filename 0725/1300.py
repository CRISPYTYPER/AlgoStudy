import sys
input = sys.stdin.readline

N = int(input())
k = int(input())

st = 1
en = N * N
while st <= en:
    mid = (st+en)//2
    cnt = 0
    for i in range(1, N+1):
        cnt += min(mid//i, N)
    if cnt >= k:
        en = mid - 1
        result = mid
    else:
        st = mid + 1
print(result)

