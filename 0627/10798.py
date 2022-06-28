word_list = [[''] * 15 for _ in range(5)]
# print(word_list)
for i in range(5):
    s = input()
    for idx,val in enumerate(s):
        word_list[i][idx]=val
# print(word_list)
for i in range(15):
    for j in range(5):
        if(word_list[j][i]!=None):
            print(word_list[j][i],end='')
print('')

# 스터디 할 내용. 파이썬에서 비어있는 인덱스를 참조하려고 하면 IndexError: list index out of range 이것 해결 방법 없을까?