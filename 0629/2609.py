a, b = map(int, input().split())
a_times_b = a * b
def get_gcd(a,b):
    if(a<b):
        temp = a
        a = b
        b = temp
    while(b>0):
        r = a % b
        a = b
        b = r
    return(a)
print(get_gcd(a,b))
print(a_times_b // get_gcd(a,b))