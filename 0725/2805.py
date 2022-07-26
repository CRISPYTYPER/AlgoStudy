import sys

input = sys.stdin.readline

n, m = map(int, input().split())
h_list = [0] + list(map(int, input().split())) # 1번 인덱스 부터 사용

# 절단기의 높이 h를 변수로 설정
# 이분탐색 알고리즘 시행
st, en = 1, max(h_list)
max_len = 0
while(st<=en):
    mid = (st+en)//2
    tree_len = 0
    for i in range(1, n + 1):
        if (h_list[i] - mid > 0):
            tree_len += h_list[i] - mid
        else:
            tree_len += 0
    if tree_len < m : # 원하는 길이만큼 안나오면(높이를 낮춰야함)
        en = mid - 1
    elif tree_len > m : # 원하는 길이보다 더 얻어지면(환경을 위해 높이 높이기. 조건은 충족됨)
        st = mid + 1
        max_len = mid
    else: #원하는 길이만큼 나오면(길이 저장하고 while문에서 걸리게끔 하기)
        st = mid + 1
        max_len = mid
print(max_len)