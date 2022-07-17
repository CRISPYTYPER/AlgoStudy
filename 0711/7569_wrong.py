from collections import deque
import sys

m,n,h = map(int, input().split()) # 가로, 세로, 높이
# 가장 밑부터 가장 위까지 순서로 주어짐
# 아이디어는 일단 다 익을 수 있는지 없는 지 여부는 익은 토마토 하나로만 가지고도 확인가능
# 최소 일수와 관련해서는 일단 다 돌려보고 제일 작은 값 찾는걸로
# 1: 익토, 0: 익않토, -1: 안들토
graph = []
ripe_cnt = 0
no_ripe_cnt = 0
no_tomato_cnt = 0
min_days = 0
bfs_cnt = 0

def bfs(z,y,x):
    dz = [-1,1,0,0,0,0] #위,아래(z),북동남서
    dy = [0,0,-1,0,1,0]
    dx = [0,0,0,0,1,0,-1]
    global ripe_cnt,no_ripe_cnt,no_tomato_cnt,bfs_cnt
    bfs_cnt += 1
    test_graph = graph.copy()
    q = deque()
    q.append((z,y,x))
    days = 0
    while q:
        now = q.popleft()
        for l in range(6):
            nz = now[0] + dz[l]
            ny = now[1] + dy[l]
            nx = now[2] + dx[l]
            if(0<=nz<h and 0<=ny<n and 0<=nx<m and test_graph[nz][ny][nx] == 0):
                q.append((nz,ny,nx))
                test_graph[nz][ny][nx] = 1 # 인접 토마토 익음
                ripe_cnt += 1
                no_ripe_cnt -= 1

        days += 1 # 하루 경과
    print(ripe_cnt,no_ripe_cnt, no_tomato_cnt)
    if (ripe_cnt + no_tomato_cnt != m * n * h and bfs_cnt == 1):
        print(-1)
        sys.exit(0)
    return days

for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int, input().split())))
    graph.append(temp)
# print(graph)
# 문제대로 초기화 완료

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                ripe_cnt += 1
            elif graph[i][j][k] == 0:
                no_ripe_cnt += 1
            elif graph[i][j][k] == -1:
                no_tomato_cnt += 1

if(ripe_cnt + no_tomato_cnt == m*n*h):
    print(0)
    sys.exit(0)

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                days = bfs(i,j,k)
                min_days = min(days, min_days)
