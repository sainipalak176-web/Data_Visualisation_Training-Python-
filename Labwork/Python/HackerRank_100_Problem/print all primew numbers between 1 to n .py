N = 20
primes = []
for num in range(2, N+1):
    is_prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
print(f" Prime numbers between 1 and {N} are:", primes)


# Output inside code:
#  Prime numbers between 1 and 20 are: [2, 3, 5, 7, 11, 13, 17, 19]