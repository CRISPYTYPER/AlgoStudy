import sys

n = int(input())
que = []
for _ in range(n):
    order = list(map(str, sys.stdin.readline().split()))
    if(order[0] == 'push'):
        que.append(order[1])
    elif(order[0] == 'pop'):
        if(len(que)):
            print(que.pop(0)) # 첫번째 요소 pop시키기
        else:
            print(-1)
    elif(order[0] == 'size'):
        print(len(que))
    elif(order[0] == 'empty'):
        if(len(que) == 0):
            print(1)
        else:
            print(0)
    elif(order[0] == 'front'):
        if(len(que)):
            print(que[0])
        else:
            print(-1)
    elif (order[0] == 'back'):
        if (len(que)):
            print(que[len(que)-1])
        else:
            print(-1)
