def remove_duplicates(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

print(remove_duplicates(lst))

# Output:
# Input:
# 5
# 1 2 2 3 1
# [1, 2, 3]