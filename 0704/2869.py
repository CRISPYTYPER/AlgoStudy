import math
a, b, v = map(int, input().split())

days = 0

if(v<=a): # 처음에 v높이 이상 올라갈 수 있으면 하루만에 올라감
    print(1)
else:
    days = 1 # 못올라갔으면 기본으로 하루는 걸림
    days += math.ceil((v-a)/(a-b))  #첫날 a만큼 올라가고, 다음날 낮까지는 (a-b)만큼 올라갔다가 다시 밤되면 떨어짐
    print(days)