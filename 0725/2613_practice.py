import sys
input = sys.stdin.readline


def get_Mgroup(target_sum):
    sum_each_group = 0
    group_cnt = 1
    for i in range(N): # 구슬들의 인덱스 순서대로 탐색
        sum_each_group += ball_lists[i]
        if sum_each_group > target_sum: # 더해가다가 그 그룹의 합이 정해진 값보다 커졌을때
            sum_each_group = ball_lists[i] # 그 구슬부터 다음 그룹으로 취급
            group_cnt += 1 # 만들어진 그룹의 수도 1 추가
    if group_cnt <= M: # 구슬들의 그룹 수가 M보다 적거나 같으면(그룹수가 적다는건 임의의 그룹의 합이 크다는 것)
        # 그룹수가 딱 M개가 되었더라도, 최소의 합을 갖도록 더 줄여봐도 됨
        return True
    else: # 구슬들의 그룹 수가 M보다 많으면(조건에 충족하지 않으므로 target_sum 값을 키워야됨. 오른쪽에서 탐색)
        return False

def cut_each_points(target_sum,M,N): # 구해진 target_sum을 가지고 구슬들을 쪼개보는 단계
    print(target_sum)
    less_than_target = 0
    ball_cnt = 0
    for i in range(N):
        less_than_target += ball_lists[i]
        if less_than_target > target_sum: # 만약 구슬들을 하나씩 grouping하다 target_sum값보다 커졌다면
            less_than_target = ball_lists[i] # 그 구슬부터 새로운 그룹 취급해줌
            M -= 1 # 하나의 그룹이 만들어졌으니 M에서 1씩 제거
            print(ball_cnt, end=' ') # 그 그룹의 구슬 수를 출력함
            ball_cnt = 0 # 새로운 그룹으로 바뀌었으니 0으로 초기화
        ball_cnt += 1 # 그룹에 구슬이 1개 추가되었으니 +1 하기

        if N-(i + 1) == M - 1: # 남은 그룹 개수가 남은 구슬 개수일때(남은 구슬은 1그룹당 1개씩 배정해야함)
            print(ball_cnt, end=" ")
            ball_cnt = 1
            M -= 1
            break

    while M:
        print(ball_cnt, end=" ")
        ball_cnt = 1
        M -= 1

N, M = map(int, input().split())
ball_lists = list(map(int, input().split()))

left_sum_limit = max(ball_lists)
right_sum_limit = sum(ball_lists)

while left_sum_limit <= right_sum_limit:
    target_sum = (left_sum_limit+right_sum_limit)//2
    if get_Mgroup(target_sum):
        right_sum_limit = target_sum - 1
    else:
        left_sum_limit = target_sum + 1

cut_each_points(left_sum_limit,M,N)