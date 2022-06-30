def get_bridges(N,M):
    result = 1
    if(N==1):
        return M
    for i in range(N):
        result *= (M-i)

    for i in range(N):
        result = result // (N-i)

    return result


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    print(get_bridges(n,m))
