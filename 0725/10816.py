import sys

def bs_start(nl, M):
    st, en = 0, len(nl)
    while(st<en):
        mid = (st+en)//2
        if(M == nl[mid]):
            en = mid
        elif(M < nl[mid]):
            en = mid
        elif(M > nl[mid]):
            st = mid + 1
    return st

def bs_end(nl, M):
    st, en = 0, len(nl)
    while(st<en):
        mid = (st+en)//2
        if(M == nl[mid]):
            st = mid + 1
        elif(M < nl[mid]):
            en = mid
        elif(M > nl[mid]):
            st = mid + 1
    return en

input = sys.stdin.readline

n = int(input())
nl = list(map(int, input().split()))
m = int(input())
ml = list(map(int, input().split()))
nl.sort()

# print(nl)

for i in ml:
    print(bs_end(nl, i) - bs_start(nl, i), end= ' ')
