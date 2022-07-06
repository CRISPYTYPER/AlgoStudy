n = int(input())

num_list = [0]
for i in range(1, n+1):
    num_list.append([0]+(list(map(int, input().split()))))
    # 0번 인덱스 안쓰도록 0번 인덱스에는 0값 추가
for i in range(n-1, 0, -1):  # n-1번째 줄부터 1번째 줄까지 순환
    for j in range(1, i+1):
        num_list[i][j] = max(num_list[i+1][j] + num_list[i][j], num_list[i+1][j+1] + num_list[i][j])
print(num_list[1][1])