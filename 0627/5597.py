submit_list = [0] * 31 # 0번 인덱스는 안쓸 예정 1-30만
nosubmit_list =[]
for _ in range(28):
    student = int(input())
    submit_list[student] += 1
for i in range(30):
    if(submit_list[i+1] == 0):
        nosubmit_list.append(i+1)
nosubmit_list.sort()
for i in nosubmit_list:
    print(i)