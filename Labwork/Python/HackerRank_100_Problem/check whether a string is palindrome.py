def is_palindrome(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return s == rev

text = input()
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")

# Output:
# Input:
# madam
# Palindrome