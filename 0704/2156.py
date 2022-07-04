import sys

n = int(input())

wine_list = [0] # 인덱스 0번 안쓸 예정. 1~n만 쓸 예정
wine_max_list = [0] * 10002
for i in range(n):
    wine_list.append(int(sys.stdin.readline())) # 문자열을 int()로 형변환하면 개행문자 사라지고 정수만 남음.
wine_list.append(0) #  맨 마지막 요소에 값 0을 추가해줌. 결과적으로 1~n+1인덱스 사용
# print(wine_list)
if(n==1):
    print(wine_list[1])
else:
    wine_max_list[1] = wine_list[1]
    wine_max_list[2] = wine_list[1] + wine_list[2]
    for i in range(3, n+1):
        wine_max_list[i] = max(wine_max_list[i-3] + wine_list[i-1] + wine_list[i], wine_max_list[i-2] + wine_list[i], wine_max_list[i-1])
        # 마지막 wine_max_list[i-1]은 i-2,i-1번에 해당하는 음료를 모두 마셔서, i번째 음료는 마실 수 없는 경우를 고려했다.
        # 이렇게 되면 i번째는 마시지 않아, i-1번째까지의 값이 i값의 고려 가능한 최댓값이다.
    # print(wine_max_list)

    print(wine_max_list[n])