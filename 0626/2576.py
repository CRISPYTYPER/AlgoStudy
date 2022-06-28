arr = []
odd_arr = []
for i in range(7):
    arr.append(int(input()))
# print(arr)
arr.sort() # 일단 배열 정렬
for i in arr:
    if(i % 2 == 1): #홀수이면
        odd_arr.append(i)
if(len(odd_arr)==0):
    print(-1)
else:
    print(sum(odd_arr))
    print(odd_arr[0])



