def first_non_repeating(s):
    for ch in s:
        if s.count(ch) == 1:
            return ch

# Input
string = "aabbcde"

# Output
print("First non-repeating character:", first_non_repeating(string))
# First non-repeating character: c