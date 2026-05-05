def unique_elements(lst):
    return list(set(lst))

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

print(unique_elements(lst))

# Output:
# Input:
# 5
# 1 2 2 3 1
# [1, 2, 3]