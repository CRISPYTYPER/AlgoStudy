n = int(input())
alpha_list = [0] * 26
for _ in range(n):
    s = input()
    first_alpha = s[0]
    first_alpha_asci = ord(first_alpha)
    alpha_list[first_alpha_asci - 97] += 1
count = 0
for idx, val in enumerate(alpha_list):
    if(val >= 5):
        print(chr(idx+97), end='')
        count += 1
if(count == 0):
    print('PREDAJA')
else:
    print('')