n = int(input())
def get_count(n):
    five_mok = n // 5
    n_temp = n
    if(n%5==0):
        return(five_mok)
    while(five_mok >= 0): # 5로 나눈 몫이 0이 될때 까지 반복
        if((n-5*five_mok)%3==0):
            return(five_mok+(n-5*five_mok)//3)
        else:
            five_mok -= 1

if(get_count(n)):
    print(get_count(n))
else:
    print(-1)