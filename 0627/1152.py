s = input().strip()
blank_count = 0
if(len(s) == 0):
    print(0)
else:
    for i in s:
        if(i == ' '):
            blank_count += 1
    print(blank_count+1)