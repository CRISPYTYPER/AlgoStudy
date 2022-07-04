import sys
n, m = map(int, input().split())
n_list = list(map(int, sys.stdin.readline().split()))
n_sum_list = [0] * 100001 # 0번 인덱스 사용 안함

n_sum_list[1] = n_list[0] # base추가

for i in range(2, n+1): # 첫번째 array부터 i번째 array까지의 합을 넣은 리스트 만들기
    n_sum_list[i] = n_sum_list[i-1] + n_list[i-1] # n_list는 n_sum_list보다 인덱스가 1 먼저 시작한다
    
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    # i, j는 1이상 n이하
    print(n_sum_list[j]-n_sum_list[i-1])

