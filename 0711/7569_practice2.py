from collections import deque

m,n,h = map(int,input().split())
a=[[list(map(int, input().split())) for i in range(n)] for depth in range(h)]

dx = [0,1,0,-1,0,0]
dy = [-1,0,1,0,0,0]
dz = [0,0,0,0,-1,1]

def bfs():
    while de:
        z,x,y = de.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0<=nx<n and 0<=ny<m and 0<=nz<h:
                if a[nz][nx][ny] == 0:
                    a[nz][nx][ny] = a[z][x][y] + 1
                    de.append([nz,nx,ny])

de = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if a[i][j][k] == 1:
                de.append([i,j,k])

bfs()

z=1
result = -1
for i in a: # i는 h개의 2차원 배열 중 하나
    for j in i: # j는 n개의 1차원 배열 중 하나
        for k in j: # k는 m개의 int 값 중 하나
            if k == 0:
                z = 0

            result=max(result,k)
if z==0: # 모두 익지 못한 상태
    print(-1)
elif result == 1: #모두 익어있는 상태
    print(0)
else:
    print(result-1)