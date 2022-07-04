n, m = map(int, input().split())
n_list = list(map(int, input().split()))

for _ in range(m):
    i, j = map(int, input().split())
    # i, j는 1이상 n이하
    count = 0
    for idx in range(i, j+1):
        count += n_list[idx-1] # idx를 0이상부터 카운팅하도록 fit
    print(count)
    count = 0
    #일단 n*m = 10^10이기에 최대 100초가 걸려 시간초과가 뜬다

