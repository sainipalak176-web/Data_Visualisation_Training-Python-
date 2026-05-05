def common_elements(l1, l2):
    common = []
    for i in l1:
        if i in l2 and i not in common:
            common.append(i)
    return common

n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))

n2 = int(input())
list2 = []
for i in range(n2):
    list2.append(int(input()))

print(common_elements(list1, list2))

# Output:
# Input:
# 3
# 1 2 3
# 3
# 2 3 4
# [2, 3]