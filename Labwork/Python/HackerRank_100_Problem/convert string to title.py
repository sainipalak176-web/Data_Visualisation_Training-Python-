def title_case(s):
    result = ""
    capitalize = True
    for ch in s:
        if ch == ' ':
            result += ch
            capitalize = True
        else:
            if capitalize:
                result += ch.upper()
                capitalize = False
            else:
                result += ch.lower()
    return result

text = input()
print(title_case(text))

# Output:
# Input:
# this is python
# This Is Python