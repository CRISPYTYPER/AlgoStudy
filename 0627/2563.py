#이거 모눈종이처럼 이차원 배열로 생각해보자
white_paper_arr = [[0] * 100 for i in range(100)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            if(white_paper_arr[y+i][x+j] == 0):
                white_paper_arr[y + i][x + j] = 1 #색 안칠해져있으면 칠하기

count = 0
for i in range(100):
    for j in range(100): #100 x 100 돌면서 색칠된 칸 수 카운트
        if(white_paper_arr[i][j] == 1):
            count += 1

print(count)