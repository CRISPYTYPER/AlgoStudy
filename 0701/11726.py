n = int(input())

tiling_list = [0]*1001 #1부터 1000번 인덱스에 담길 예정
# 재귀로 푸는 것 보다는 이렇게 리스트에 담아 나중에 참조할 수 있도록 해주는게 연산의 양을 줄일 수 있다
# 메모이제이션이랄까
tiling_list[1] = 1
tiling_list[2] = 2
for i in range(3, n+1):
    tiling_list[i] = (tiling_list[i-1] + tiling_list[i-2]) % 10007

print(tiling_list[n])
