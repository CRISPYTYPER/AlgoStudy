import sys

n = int(input())

num_list = [i for i in range(1,n+1)] # 1~n까지 수를 담은 리스트

stack = [] # 테스트를 위한 스택
pp_list = [] # +,-를 집어넣을 예정

list_input = [] # 입력받을 인풋
for i in range(n):
    list_input.append(int(input()))

cnt = 0 #list의 인덱스
for i in num_list: # 1~n까지 반복
    if list_input[cnt] > i:
        stack.append(i)
        pp_list.append('+')  # push
    elif list_input[cnt] == i:
        stack.append(i)
        pp_list.append('+')  # push
        stack.pop()
        pp_list.append('-')  # pop
        cnt += 1
    elif list_input[cnt] < i: # 예제 1 에서는 i가 5일때의 경우
        i = num_list[i-1]
        temp = stack.pop() # 3
        if temp != list_input[cnt]:
            print('NO')
            sys.exit(0)
        elif temp == list_input[cnt]:
            pp_list.append('-')  # pop
            cnt += 1


print(pp_list)

