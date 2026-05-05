# =====================================
# Problem 41: Check prime number using function
# =====================================

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

num = 7
print("Problem 41 - Is Prime:", is_prime(num))

# Output:
# Problem 41 - Is Prime: True


# =====================================
# Problem 42: Find factorial using function
# =====================================

def factorial(n):
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    return fact

num = 5
print("Problem 42 - Factorial:", factorial(num))

# Output:
# Problem 42 - Factorial: 120


# =====================================
# Problem 43: Check palindrome string using function
# =====================================

def is_palindrome(s):
    return s == s[::-1]

text = "madam"
print("Problem 43 - Is Palindrome:", is_palindrome(text))

# Output:
# Problem 43 - Is Palindrome: True


# =====================================
# Problem 44: Find maximum of three numbers using function
# =====================================

def max_of_three(a, b, c):
    return max(a, b, c)

a, b, c = 10, 25, 15
print("Problem 44 - Maximum number:", max_of_three(a, b, c))

# Output:
# Problem 44 - Maximum number: 25


# =====================================
# Problem 45: Find sum of digits using function
# =====================================

def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

num = 1234
print("Problem 45 - Sum of digits:", sum_of_digits(num))

# Output:
# Problem 45 - Sum of digits: 10


# =====================================
# Problem 46: Generate Fibonacci series using function
# =====================================

def fibonacci(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

n = 7
print("Problem 46 - Fibonacci series:", fibonacci(n))

# Output:
# Problem 46 - Fibonacci series: [0, 1, 1, 2, 3, 5, 8]


# =====================================
# Problem 47: Count vowels using function
# =====================================

def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count

text = "Education"
print("Problem 47 - Vowel count:", count_vowels(text))

# Output:
# Problem 47 - Vowel count: 5