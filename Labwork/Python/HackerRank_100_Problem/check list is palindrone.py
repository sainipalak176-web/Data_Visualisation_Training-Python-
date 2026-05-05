def is_palindrome_list(lst):
    return lst == lst[::-1]

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

if is_palindrome_list(lst):
    print("Palindrome List")
else:
    print("Not Palindrome List")

# Output:
# Input:
# 5
# 1 2 3 2 1
# Palindrome List