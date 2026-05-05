def sort_list(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

print(sort_list(lst))

# Output:
# Input:
# 5
# 5 2 4 1 3
# [1, 2, 3, 4, 5]