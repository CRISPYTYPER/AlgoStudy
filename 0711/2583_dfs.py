import sys
sys.setrecursionlimit(20000)
area_list = []
area = 0
cnt = 0
def dfs(y,x):
    global area
    area += 1
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]  # 북동남서
    for l in range(4):
        next_x = x+dx[l]
        next_y = y+dy[l]
        if(0<=next_x<n and 0<=next_y<m and graph[next_y][next_x] == 0):
            graph[next_y][next_x] = -1
            dfs(next_y,next_x)

m,n,k = map(int, input().split())
graph = [[0] * n for _ in range(m)]
for _ in range(k):
    fx, fy, sx, sy = map(int, input().split())
    for i in range(sy-fy):
        for j in range(sx-fx): # 만들어진 직사각형은 (sy-fy), (sx-fx)의 길이의 변으로 이루어짐
            if(graph[fy+i][fx+j] == 0):
                graph[fy + i][fx + j] = 1 # 직사각형 칠해주기
#여기까지가 문제 초기화

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0: #분리된 영역 찾았으면
            graph[i][j] = -1
            area = 0
            dfs(i,j)
            area_list.append(area)
            cnt += 1

print(cnt)
print(*sorted(area_list))