def average_list(lst):
    total = 0
    for i in lst:
        total += i
    return total / len(lst)

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

print(average_list(lst))

# Output:
# Input:
# 4
# 10 20 30 40
# 25.0