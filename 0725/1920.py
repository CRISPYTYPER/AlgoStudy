n = int(input())
nl = list(map(int, input().split()))
m = int(input())
ml = list(map(int, input().split()))

nl.sort()
# print(nl)

def binary_search(nl, M):
    st, en = 0, len(nl) - 1  # nl의 처음과 끝 인덱스
    while st <= en:
        mid = (st + en) // 2  # 홀수개의 인덱스면 가운데, 짝수개의 인덱스면 중간 2개중 앞의것
        if (M == nl[mid]):
            return 1
        elif(M < nl[mid]):
            en = mid - 1
        elif(M > nl[mid]):
            st = mid + 1
    return 0


for i in ml:
    print(binary_search(nl,i))

