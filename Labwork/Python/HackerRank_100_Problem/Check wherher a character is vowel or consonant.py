#check whether a character is vowel or consonant.
# List of characters to test
char_list = ['a', 'E', 'k', 'O', 'z']

for ch in char_list:
    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        print(f" {ch} is a Vowel")
    else:
        print(f" {ch} is a Consonant")

# Output :
"""a is a Vowel"""
"""E is a Vowel"""
"""k is a Consonant"""
"""O is a Vowel"""
"""z is a Consonant"""