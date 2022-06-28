s = input()
alphabet_list = [0] * 26
for i in s:
    alphabet_list[ord(i)-97] += 1 # 'a'의 아스키 코드는 97
for i in range(26):
    print(alphabet_list[i], end=' ')