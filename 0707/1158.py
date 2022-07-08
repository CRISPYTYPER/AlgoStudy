n, k = map(int, input().split())

num_list = []  # 처음에 입력받을 리스트
pop_list = []  # 제거된 사람들 담는 리스트
for i in range(n):
    num_list.append(i+1)  # 리스트에 n개의 숫자 집어넣기

remove_index = 0  # 제거할 위치 인덱스 초기값


while(len(num_list)):  # 리스트의 길이가 존재할때 까지(다시말하면 요소 없어질때까지 반복)
    remove_index = (remove_index + (k - 1)) % n
    # 지워진 요소 자리를 그 뒤의 수들이 채울 것이므로, k-1을 더하는 것이 맞음.
    # 1 2 3 4 5 6 7 (3이 2번 인덱스였는데 아래에서는 지워지고 4가 2번 인덱스가 됨)
    # 1 2 4 5 6 7
    pop_list.append(num_list[remove_index])
    del num_list[remove_index]
    n -= 1

# print(pop_list)

result_string = '<'
for num in pop_list:
    result_string += str(num) + ', '

result_string = result_string.rstrip(', ')  # 오른쪽 (', ) 삭제
result_string += '>'
print(result_string)

# print('<' + ', '.join(map(str, pop_list)) + '>')
# 한줄짜리는 다른사람들 코드 보고 넣은건데 파이썬 기능들을 익힐 필요가 있겠다.
