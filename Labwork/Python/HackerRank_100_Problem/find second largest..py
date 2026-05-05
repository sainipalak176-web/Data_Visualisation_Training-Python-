def second_largest(lst):
    largest = second = -999999
    for i in lst:
        if i > largest:
            second = largest
            largest = i
        elif i > second and i != largest:
            second = i
    return second

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

print(second_largest(lst))

# Output:
# Input:
# 5
# 10 20 30 40 50
# 40