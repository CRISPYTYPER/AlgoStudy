import sys
input = sys.stdin.readline

def is_possible(target):
    grpCnt = 1
    total = 0
    for number in numbers:
        total += number
        if total > target:
            grpCnt += 1
            total = number
    return grpCnt <= M # 만들어진 그룹수가 M보다 작거나 같으면 True

def solve(target):
    count = 0
    total = 0
    result = []
    m = M
    for idx in range(N):
        total += numbers[idx]
        if total > target:
            m -= 1
            total = numbers[idx]
            result.append(count)
            count = 0
        count += 1
        if N - idx == m:
            break

    while m:
        result.append(count)
        count = 1
        m -= 1
    return result

N, M = map(int, input().split()) # N: 구슬들의 수, M: 나눌 그룹 수
numbers = list(map(int, input().split())) # 각 구슬에 적혀진 숫자 리스트
left = max(numbers)
right = sum(numbers)

while left <= right:
    mid = (left+right) // 2
    if is_possible(mid):
        right = mid - 1
    else:
        left = mid + 1

print(left)
print(*(solve(left)))
