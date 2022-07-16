t = int(input())
m, n, k = map(int, input().split())
# 아래 리스트에는 배추들의 x, y 좌표 담을 예정
baechu_list = [[]]  # 0번 인덱스는 사용 안함
for i in range(k):
    baechu_list.append(list(map(int, input().split())))
