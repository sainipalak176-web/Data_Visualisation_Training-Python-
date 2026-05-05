def merge_unique(l1, l2):
    merged = l1 + l2
    result = []
    for i in merged:
        if i not in result:
            result.append(i)
    return result

n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))

n2 = int(input())
list2 = []
for i in range(n2):
    list2.append(int(input()))

print(merge_unique(list1, list2))

# Output:
# Input:
# 3
# 1 2 3
# 3
# 2 3 4
# [1, 2, 3, 4]