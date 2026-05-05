def tuple_to_list(t):
    return list(t)

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
tpl = tuple(lst)

print(tuple_to_list(tpl))

# Output:
# Input:
# 3
# 1 2 3
# [1, 2, 3]