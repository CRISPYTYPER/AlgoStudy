s = input()
alpha_count = [0] * 26
for alpha in s:
    asci = ord(alpha)  # 알파벳을 아스키로
    # 대문자 알파벳 65~90
    # 소문자 알파벳 97~122
    if (asci >= 65 and asci <= 90):  # 대문자 알파벳이면
        alpha_count[asci - 65] += 1
    elif (asci >= 97 and asci <= 122):
        alpha_count[asci - 97] += 1
# print(alpha_count)
max_count = 0 #알파벳 최대 개수
max_duple = 0 #중복된 최대 알파벳 수
max_index = -1 #최대 알파벳 인덱스

# 알파벳들 개수 리스트에 집어넣기 완료
for idx, val in enumerate(alpha_count):
    if(val>max_count): # 최댓값 신기록 갱신하면
        max_count = val
        max_duple = 1
        max_index = idx
    elif(val == max_count): #최댓값 중복된게 나오면
        max_duple += 1
        max_index = '?' # 파이썬이라는 언어의 특징. 동적 프로그래밍 언어. 프로그램 실행중에 변수의 타입을 동적으로 바꿀 수 있다.(스터디때 다루면 좋을듯)

if(max_duple == 1):
    print(chr(max_index+65))
else:
    print(max_index)