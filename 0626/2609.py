a, b = map(int, input().split())

if(b>a): # a를 큰 값으로 맞추기 위함
    temp = b
    b = a
    a = temp
# 유클리드 알고리즘 적용
# GCD(a,b) = GCD(b,a%b)
first_a = a
first_b = b
while(b!=0):
    r = a % b
    a = b
    b = r
print(a) # 최대공약수
print(first_a*first_b//a) # 최대공배수 (미리 약분시켰음)