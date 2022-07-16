import sys
from collections import deque

def bfs(y,x):
    q = deque()
    q.append((y,x))
    while q:
        now = q.popleft()
        for l in range(4):
            hh = now[0] + dh[l]
            ww = now[1] + dw[l]
            if 0 <= ww < w and 0 <= hh < h and graph[hh][ww] == 1:
                graph[hh][ww] = 0
                q.append((hh, ww))

dw = [0, 1, 0, -1]
dh = [-1, 0, 1, 0]
read = sys.stdin.readline
T = int(read())
for _ in range(T):
    w, h, k = map(int, read().split())
    graph = [[0]*w for _ in range(h)]
    result = 0
    for _ in range(k):
        x, y = map(int, read().split())
        graph[y][x] = 1
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                graph[i][j] = 0
                bfs(i, j)
                result += 1
    print(result)

