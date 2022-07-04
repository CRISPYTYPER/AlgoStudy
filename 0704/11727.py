n = int(input())

tile_list = [0] * 1001

tile_list[1] = 1
tile_list[2] = 3

for i in range(3,1001):
    tile_list[i] = (tile_list[i-1] + 2*tile_list[i-2]) % 10007
print(tile_list[n])