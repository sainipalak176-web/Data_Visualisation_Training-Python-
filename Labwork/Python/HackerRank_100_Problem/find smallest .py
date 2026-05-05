def smallest(lst):
    return min(lst)

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

print(smallest(lst))

# Output:
# Input:
# 5
# 10 25 5 40 15
# 5