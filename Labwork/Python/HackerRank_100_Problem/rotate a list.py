def rotate_list(lst, k):
    k = k % len(lst)
    return lst[k:] + lst[:k]

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

k = int(input())
print(rotate_list(lst, k))

# Output:
# Input:
# 5
# 1 2 3 4 5
# 2
# [3, 4, 5, 1, 2]