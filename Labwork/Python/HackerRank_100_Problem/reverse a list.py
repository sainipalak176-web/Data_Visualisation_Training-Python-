def reverse_list(lst):
    rev = []
    for i in range(len(lst)-1, -1, -1):
        rev.append(lst[i])
    return rev

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

print(reverse_list(lst))

# Output:
# Input:
# 4
# 1 2 3 4
# [4, 3, 2, 1]