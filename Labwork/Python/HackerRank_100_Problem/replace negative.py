def replace_negative(lst):
    result = []
    for i in lst:
        if i < 0:
            result.append(0)
        else:
            result.append(i)
    return result

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

print(replace_negative(lst))

# Output:
# Input:
# 5
# -1 2 -3 4 -5
# [0, 2, 0, 4, 0]