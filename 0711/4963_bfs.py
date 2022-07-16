from collections import deque

def bfs(y,x):
    global w, h
    q = deque()
    q.append((y,x))
    while q:
        now = q.popleft()
        for l in range(8):
            ny = now[0] + dh[l]
            nx = now[1] + dw[l]
            if (0 <= nx < w and 0 <= ny < h and graph[ny][nx] == 1):
                graph[ny][nx] = -1
                q.append((ny,nx))

def main():
    global w, h, graph
    while(1):
        w, h = map(int, input().split())
        if(w == 0 and h == 0): # 끝내는 부분
            return
        graph = [] # 땅 초기화
        for i in range(h):
            graph.append(list(map(int, input().split()))) # 섬과 바다를 받음
        island_num = 0
        for i in range(h):
            for j in range(w):
                if(graph[i][j] == 1): # 섬을 찾으면
                    graph[i][j] = -1 # 탐색을 완료했다고 표시
                    bfs(i,j)
                    island_num += 1
        print(island_num)
#위에서부터 시계방향으로 돌기
dw = [0,1,1,1,0,-1,-1,-1]
dh = [-1,-1,0,1,1,1,0,-1]
global w, h, graph
main()