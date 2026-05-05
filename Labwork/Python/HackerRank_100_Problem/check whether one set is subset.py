def is_subset(s1, s2):
    return s1.issubset(s2)

n1 = int(input())
s1 = set()
for i in range(n1):
    s1.add(int(input()))

n2 = int(input())
s2 = set()
for i in range(n2):
    s2.add(int(input()))

if is_subset(s1, s2):
    print("Subset")
else:
    print("Not Subset")

# Output:
# Input:
# 2
# 1 2
# 4
# 1 2 3 4
# Subset