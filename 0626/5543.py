burger_arr = []
drink_arr = []
sum_arr = []
for _ in range(3):
    burger_arr.append(int(input()))
for _ in range(2):
    drink_arr.append(int(input()))

for i in burger_arr:
    for j in drink_arr:
        sum_arr.append(i+j-50)
sum_arr.sort()
print(sum_arr[0])