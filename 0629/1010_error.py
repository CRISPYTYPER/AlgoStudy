def factorial(N):
    if(N == 1):
        return(1)
    else:
        return N*factorial(N-1)

def get_bridges(N, M):
    bridge_num = int(factorial(N) / factorial(M) / factorial(N-M))
    return  bridge_num

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    print(get_bridges(n,m))

'''
Traceback (most recent call last):
  File "E:\Algorithm\CodingStudy\0629\1010.py", line 15, in <module>
    print(get_bridges(n,m))
  File "E:\Algorithm\CodingStudy\0629\1010.py", line 8, in get_bridges
    bridge_num = int(factorial(N) / factorial(M) / factorial(N-M))
  File "E:\Algorithm\CodingStudy\0629\1010.py", line 5, in factorial
    return N*factorial(N-1)
  File "E:\Algorithm\CodingStudy\0629\1010.py", line 5, in factorial
    return N*factorial(N-1)
  File "E:\Algorithm\CodingStudy\0629\1010.py", line 5, in factorial
    return N*factorial(N-1)
  [Previous line repeated 994 more times]
  File "E:\Algorithm\CodingStudy\0629\1010.py", line 2, in factorial
    if(N == 1):
RecursionError: maximum recursion depth exceeded in comparison
'''