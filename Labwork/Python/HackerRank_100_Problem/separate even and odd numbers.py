def separate_even_odd(lst):
    even = []
    odd = []
    for i in lst:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

even, odd = separate_even_odd(lst)
print("Even:", even)
print("Odd:", odd)

# Output:
# Input:
# 5
# 1 2 3 4 5
# Even: [2, 4]
# Odd: [1, 3, 5]