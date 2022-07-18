import sys
from collections import deque

input = sys.stdin.readline

# m: 가로, n: 세로, h: 높이
m,n,h = map(int, input().split())

graph = []
q = deque()

def bfs():
    directions = [(1,0,0),(-1,0,0),(0,-1,0),(0,0,1),(0,1,0),(0,0,-1)]
    while q:
        now_h, now_n, now_m = q.popleft()
        for l in range(6):
            next_h = now_h + directions[l][0]
            next_n = now_n + directions[l][1]
            next_m = now_m + directions[l][2]
            if(0<=next_h<h and 0<=next_n<n and 0<=next_m<m):
                if(graph[next_h][next_n][next_m] == 0): # 익은 사과 옆에 있는 안익은 사과면
                    graph[next_h][next_n][next_m] = graph[now_h][now_n][now_m] + 1
                    q.append((next_h,next_n,next_m))
                    # 최초 익은 사과 옆의 안익은 사과는 2가 됨



for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int, input().split())))
        for k in range(m):
            if temp[j][k] == 1:
                # 익은 사과가 발견될 경우, 해당 사과의 (z,y,x)좌표를 큐에 집어넣어줌. 나중에 bfs 돌릴 예정
                q.append((i,j,k))
    graph.append(temp)

bfs()

# print(graph)
days = -1
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print(-1)
                sys.exit(0)
            else:
                days = max(days, graph[i][j][k])

print(days-1)


