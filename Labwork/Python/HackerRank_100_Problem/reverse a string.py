def reverse_string(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev

text = input()
print(reverse_string(text))

# Output:
# Input:
# hello
# olleh