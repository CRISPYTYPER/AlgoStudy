n = int(input())

days_list = [0] * 100001

for i in range(2019,100001):
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (i % 100 == 0 and i % 400 != 0):  # 윤년 아님
        pass
    elif (i % 400 == 0):  # 윤년임
        month_days[2] += 1
    elif (i % 100 != 0 and i % 4 == 0):  # 윤년임
        month_days[2] += 1
    else:  # 윤년 아님
        pass
    days_list[i] = month_days
# print(days_list)
#월화수목금토일 -> 0~6으로 매핑. 금요일은 4
#2019년 1월 1일 화요일 기준

yoil = 1
cnt = 0 #13일의 금요일 누적 개수
for i in range(2019,n+1):
    for j in range(1,12+1):
        for k in range(1, days_list[i][j]+1): #날짜별 반복
            if(yoil == 4 and k == 13):
                cnt += 1
            yoil = (yoil + 1) % 7

print(cnt)