num = 153
order = len(str(num))
sum_digits = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum_digits += digit ** order
    temp //= 10

if sum_digits == num:
    print(f" {num} is an Armstrong number")
else:
    print(f" {num} is NOT an Armstrong number")

    
# Output inside code:
# Problem 26 - 153 is an Armstrong number