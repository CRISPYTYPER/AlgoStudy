# 재귀 limit 설정
import sys
sys.setrecursionlimit(10000)

# dfs 정의
def dfs(x, y):
    # 상하좌우 확인을 위해 dx, dy 생성
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    # 네 방향 탐색
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if(0 <= next_x < M) and (0 <= next_y < N):
            if(graph[next_y][next_x] == 1):
                graph[next_y][next_x] = -1
                dfs(next_x,next_y)

T = int(input())

for i in range(T):
    M, N, K = map(int, input().split())  # M:가로, N:세로, K:개수
    graph = [[0]*M for i in range(N)]
    cnt = 0

    # 배추 위치에 1 표시
    for j in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1

    # dfs 활용해서 배추 그룹 수 세기
    for x in range(M):
        for y in range(N):
            if graph[y][x] == 1:
                dfs(x, y)
                cnt += 1
    print(cnt)