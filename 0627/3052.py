div_list = []

for _ in range(10):
    div_list.append(int(input())%42)

div_set = set(div_list)

print(len(div_set))