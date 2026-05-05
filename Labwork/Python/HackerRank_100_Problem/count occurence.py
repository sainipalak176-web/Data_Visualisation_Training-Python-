def count_occurrence(t, x):
    return t.count(x)

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
t = tuple(lst)

x = int(input())
print(count_occurrence(t, x))

# Output:
# Input:
# 5
# 1 2 3 2 2
# 2
# 3