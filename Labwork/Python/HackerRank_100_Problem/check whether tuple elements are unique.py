def is_unique(t):
    return len(t) == len(set(t))

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
t = tuple(lst)

if is_unique(t):
    print("Unique Elements")
else:
    print("Not Unique Elements")

# Output:
# Input:
# 4
# 1 2 3 4
# Unique Elements