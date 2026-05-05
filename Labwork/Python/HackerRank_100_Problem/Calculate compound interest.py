#calculate compound interest.
# Given values
principal = 10000  # Principal amount in rupees
rate = 5            # Annual interest rate in percent
time = 3            # Time in years
n = 1               # Compounded once per year

# Compound Interest formula: A = P * (1 + R/100)^T
amount = principal * (1 + rate/100)**time
compound_interest = amount - principal

print(" Compound Interest is:", round(compound_interest, 2))


#output:
"""the compound interest is :1576.25"""

