n = int(input())

biary_list = [0] * 1000001

biary_list[1] = 1
biary_list[2] = 2

for i in range(3, n+1):
    biary_list[i] = (biary_list[i-1] + biary_list[i-2]) % 15746

print((biary_list[n]))
