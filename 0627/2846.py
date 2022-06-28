n = int(input())
height_list = list(map(int, input().split()))

max_ormak= 0
ormak = 0
prev_height = height_list[0]
for idx, height in enumerate(height_list):
    if(idx!=0):
        if(prev_height < height): # 처음 아니고 전 높이보다 높으면
            ormak += (height-prev_height)
            if(idx==len(height_list)-1):#마지막 높이이면
                if (max_ormak < ormak):  # 최고 오르막이면
                    max_ormak = ormak  # 최고 오르막 갱신
        elif(prev_height >= height):
            if(max_ormak<ormak): #최고 오르막이면
                max_ormak = ormak # 최고 오르막 갱신
            ormak = 0 # 현 오르막길 크기 초기화

    prev_height = height
print(max_ormak)

