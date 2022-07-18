import sys

n = int(input())

input_list = [] # 입력된 수열
test_stack = [] # input_list처럼 만들어보려고 시도해보는 stack이다.
result_list =[] # 맞게 출력되나 확인해보려고 만든 리스트이다.
pp_list = [] # +,-를 넣는 리스트이다
input_idx = 0 # input_list의 인덱스 값이다
num = 1 # 1~n까지 증가하는 수이다
for i in range(n): # input_list에 입력을 받는다
    input_list.append(int(input()))

while(len(test_stack)!=n): # test_stack이 n의 요소를 가질때까지 반복한다
    if input_idx >= len(input_list):
        break

    if num < input_list[input_idx]: # idx의 값이 input_list의 요소와 같아질때까지 스택에 넣어준다
        test_stack.append(num)
        pp_list.append('+')
        num += 1
    elif num == input_list[input_idx]:  # idx의 값이 input_list의 요소와 같아지면
        #스택에 넣었다가 결과 리스트에 담아준다
        test_stack.append(num)
        pp_list.append('+')
        result_list.append(test_stack.pop())
        pp_list.append('-')
        input_idx += 1 # 그 요소는 찾았으니 다음 요소로 넘어감
        num += 1
    elif num > input_list[input_idx]:
        if len(test_stack) == 0:
            print('NO')
            sys.exit(0)
        temp = test_stack.pop()

        if input_list[input_idx] == temp:
            result_list.append(temp)
            pp_list.append('-')
            input_idx += 1  # 그 요소는 찾았으니 다음 요소로 넘어감
        else:
            print('NO')
            sys.exit(0)
for i in pp_list:
    print(i)
    



