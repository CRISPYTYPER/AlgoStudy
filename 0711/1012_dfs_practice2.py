# 재귀 limit 설정
import sys
sys.setrecursionlimit(10000)

# dfs 정의
def dfs(y, x):
    #북동남서 확인을 위해 dx, dy 생성
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]

    #네 방향 탐색
    for l in range(4):
        nx = x + dx[l]
        ny = y + dy[l]
        if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 1:
            graph[ny][nx] = -1 # 배추가 인접할 때 체커
            dfs(ny, nx)

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]
    cnt = 0

    # 배추 위치에 1 표시
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1

    #dfs 활용해서 배추 그룹 수 세기
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1:
                graph[y][x] = -1
                cnt += 1
                dfs(y, x)

    print(cnt)