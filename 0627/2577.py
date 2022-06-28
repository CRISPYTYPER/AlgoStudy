a = int(input())
b = int(input())
c = int(input())
multiple = a*b*c
numcount_list = [0 for i in range(10)]
multiple_str = str(multiple)
for i in multiple_str:
    numcount_list[int(i)]+=1

for i in range(10):
    print(numcount_list[i])

