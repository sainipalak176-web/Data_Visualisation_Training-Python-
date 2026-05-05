def only_digits(s):
    for ch in s:
        if ch < '0' or ch > '9':
            return False
    return True

text = input()
if only_digits(text):
    print("Only Digits")
else:
    print("Not Only Digits")

# Output:
# Input:
# 12345
# Only Digits