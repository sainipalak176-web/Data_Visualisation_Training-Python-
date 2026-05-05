def replace_vowels(s):
    result = ""
    for ch in s:
        if ch.lower() in 'aeiou':
            result += '*'
        else:
            result += ch
    return result

text = input()
print(replace_vowels(text))

# Output:
# Input:
# education
# *d*c*t**n