import sys
from collections import deque

input = sys.stdin.readline
m,n,h = map(int, input().split())
arr=[]
q = deque()
for i in range(h):
    temp=[]
    for j in range(n):
        temp.append(list(map(int, input().split())))
        for k in range(m):
            if temp[j][k] == 1:
                q.append((i,j,k))
    arr.append(temp)


# 6방향
directions = [(1,0,0),(-1,0,0),(0,-1,0),(0,0,1),(0,1,0),(0,0,-1)]

while q: # bfs 실행
    hh, nn, mm = q.popleft()
    for l in range(6):
        hhh = hh + directions[l][0]
        nnn = nn + directions[l][1]
        mmm = mm + directions[l][2]
        if 0<=hhh<h and 0<=nnn<n and 0<=mmm<m and arr[hhh][nnn][mmm] == 0: # 익힐 수 있는 토마토면
            q.append((hhh,nnn,mmm))
            arr[hhh][nnn][mmm] = arr[hh][nn][mm] + 1 #1 주변은 2로 만듬

result = 0 # 며칠 걸리는지

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 0: # 익지 않은 토마토 발견 시
                print(-1)
                exit(0)
            else:
                result = max(result, arr[i][j][k])

print(result-1)



