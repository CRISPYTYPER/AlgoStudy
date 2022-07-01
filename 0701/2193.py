n = int(input())

ichin_list = [0]*91 #1부터 90번 인덱스에 담길 예정
# 재귀로 푸는 것 보다는 이렇게 리스트에 담아 나중에 참조할 수 있도록 해주는게 연산의 양을 줄일 수 있다
# 메모이제이션이랄까
ichin_list[1] = 1
ichin_list[2] = 1
for i in range(3, n+1):
    ichin_list[i] = ichin_list[i-1] + ichin_list[i-2]

print(ichin_list[n])
