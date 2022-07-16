from collections import deque
import sys
sys.setrecursionlimit(2000)

def dfs(node):
    dfs_visit_list[node] = 1
    print(node, end=' ')
    for i in range(1, n+1):
        if(dfs_visit_list[i] == 0 and graph[node][i] == 1):
            #방문 안했었고, 노드끼리 이어져 있으면
            dfs(i)
def bfs(node):
    q = deque()
    q.append(node)
    bfs_visit_list[node] = 1
    while q:
        node = q.popleft()
        print(node, end=' ')
        for i in range(1, n+1):
            if(bfs_visit_list[i] == 0 and graph[node][i] == 1):
                q.append(i)
                bfs_visit_list[i] = 1


n,m,v = map(int, input().split())
dfs_visit_list = [0] * (n+1)
bfs_visit_list = [0] * (n+1)
# 정점 번호는 1번부터 n번까지
graph = [[0]*(n+1)for _ in range(n+1)] #0번인덱스는 사용 안함
for _ in range(m):
    v1, v2 = map(int, input().split())
    if(graph[v1][v2] == 0): # graph[v1][v2] 하나만 확인해도됨. 대칭이니까
        graph[v1][v2] = graph[v2][v1] = 1  #정점 사이 간선 표시
# 문제 초기화 완료
dfs(v)
print()
bfs(v)
