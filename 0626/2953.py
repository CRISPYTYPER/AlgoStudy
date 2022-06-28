chef_list = []
for i in range(5):
    score = sum(list(map(int, input().split())))
    # print(score)
    chef_list.append(score)
top_chef_num = 1
top_chef_score = chef_list[top_chef_num-1]
# print(chef_list)
for idx,val in enumerate(chef_list):
    if(top_chef_score<val):
        top_chef_num = idx + 1
        top_chef_score = val
print(top_chef_num, top_chef_score)