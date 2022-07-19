for i in range(3):
    s = input()
    dup_num = s[0] # 중복된 숫자
    max_cnt = 1 # 최대 중복 수 카운팅
    temp_cnt = 1
    for idx, a in enumerate(s):
        if(idx == 0):
            continue
        if a == dup_num and a == s[idx-1]: # 전 숫자와 똑같으면
            temp_cnt += 1
        else:
            max_cnt = max(max_cnt, temp_cnt)
            temp_cnt = 1
            dup_num = a
        if idx == len(s)-1:
            max_cnt = max(max_cnt, temp_cnt)
    print(max_cnt)
