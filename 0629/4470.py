def get_line_number(s, idx):
    idx_string = '%i. %s' %(idx, s)
    return (idx_string)


n = int(input())

for i in range(n):
    s = input()
    print(get_line_number(s, i+1))