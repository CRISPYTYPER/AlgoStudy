n = int(input())
pinary_list = [0] * 91
pinary_list[1] = 1
pinary_list[2] = 1

if(n>=3):
    for i in range(3, n+1):
        pinary_list[i] = pinary_list[i-1] + pinary_list[i-2]
print(pinary_list[n])