n = int(input())
ones = 0
zeros = 0
for i in range(n):
    number = int(input())
    if(number == 1):
        ones += 1
    elif(number == 0):
        zeros += 1
if(zeros>ones):
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')