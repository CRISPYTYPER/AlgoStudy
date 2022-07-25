import sys

input = sys.stdin.readline

n = int(input())
nl = list(map(int, input().split()))
m = int(input())
ml = list(map(int, input().split()))
nl.sort()

def binary_search(nl, M):
    st, en = 0, len(nl)-1
    while(st<=en):
        mid = (st+en)//2
        if(M == nl[mid]):
            return 1
        elif(M < nl[mid]):
            en = mid - 1
        elif(M > nl[mid]):
            st = mid + 1
    return 0

for i in ml:
    print(binary_search(nl, i), end=' ')