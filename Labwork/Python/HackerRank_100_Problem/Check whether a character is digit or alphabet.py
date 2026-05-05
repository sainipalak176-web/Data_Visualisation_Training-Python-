#check whether a character is digit or alphabet.
# List of characters to test
char_list = ['A']

for ch in char_list:
    if ch.isdigit():
        print(f"Problem 14 - {ch} is a Digit")
    elif ch.isalpha():
        print(f" {ch} is an Alphabet")
    else:
        print(f" {ch} is neither Digit nor Alphabet")



    #output:
"""A is an alphabet"""
