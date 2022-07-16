import sys
sys.setrecursionlimit(10000)

def dfs(y,x):
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    for k in range(4):
        next_x = x + dx[k]
        next_y = y + dy[k]
        if 0 <= next_x < M and 0 <= next_y < N and ground_list[next_y][next_x] == 1:
            ground_list[next_y][next_x] = 0
            dfs(next_y, next_x)

T = int(input())
for _ in range(T):
    jirungi_num = 0
    M, N, K = map(int, input().split())
    ground_list = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        ground_list[y][x] = 1 # 배추심기

    for i in range(N):
        for j in range(M):
            if ground_list[i][j] == 1:
                ground_list[i][j] = 0
                jirungi_num += 1
                dfs(i, j)
    print(jirungi_num)
