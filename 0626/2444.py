n = int(input())

for i in range(n):
    for _ in range(n-i-1):
        print(' ',end='')
    for _ in range(2*i+1):
        print('*', end='')
    print('')
for j in range(n-1):
    for _ in range(j+1):
        print(' ',end='')
    for _ in range(2*(n-j)-3):
        print('*', end='')
    print('')