import itertools

n = int(input())

# permutation = 1
# for i in range(n):
#     permutation *= (n - i)
#
num_list = list(map(int, input().split()))
num_list.sort()

list_permutations = list(itertools.permutations(num_list, n))
max_result = 0
for i in list_permutations:
    temp = 0
    for j in range(1, len(i)):
        temp += abs(i[j-1]-i[j])
    max_result = max(max_result,temp)

print(max_result)