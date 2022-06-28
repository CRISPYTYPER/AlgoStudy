s = input()
alphabet_list = [-1] * 26
for idx,val in enumerate(s):
    if(alphabet_list[ord(val)-97] == -1 ): #아직 안찾아진 알파벳이면
        alphabet_list[ord(val) - 97] = idx
for i in alphabet_list:
    print(i,end=' ')