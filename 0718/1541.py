s = input()

# - 가 나오면 다음 - 가 나오기 전까지 괄호로 묶어주면 될듯
total = 0
minus_flag = False
temp_str = ''
for idx, i in enumerate(s):
    if(i == '-'):
        if (minus_flag == True): # - 뒤에 -가 붙었으면 그 사이의 값은 빼준다(-사이에 괄호친것)
            total -= int(temp_str)
            temp_str = ''
        elif (minus_flag == False): # 처음으로 만나는 - 면 그전까지의 값은 더해준다.
            total += int(temp_str)
            minus_flag = True
            temp_str = ''
    elif(i == '+'):
        if(minus_flag == True):
            total -= int(temp_str) # -로 출발했는데, +가 나왔다면 -부터 다음 -가 나올때까지 괄호로 묶이니 + 는 -로 묶인다.
            temp_str = ''
        elif(minus_flag == False): # -가 한번도 안나왔는데 + 를 만나면 더해주는 방법밖에 없다.
            total += int(temp_str)
            temp_str = ''
    else: # 숫자가 인풋이면
        temp_str += i
        if(idx == len(s)-1):
            if (minus_flag == True):
                total -= int(temp_str)
            elif (minus_flag == False):
                total += int(temp_str)
print(total)