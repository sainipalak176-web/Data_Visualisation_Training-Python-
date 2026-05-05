# Salary Processing System
salaries = [25000, 48000, 52000, 61000, 45000, 72000, 39000]
minimum_wage = 30000
# 1. Remove salaries below minimum wage
valid_salaries = []
for sal in salaries:
    if sal >= minimum_wage:
        valid_salaries.append(sal)
print("Valid Salaries:", valid_salaries)
# 2. Add 5% bonus to employees with salary > 50000
for i in range(len(valid_salaries)):
    if valid_salaries[i] > 50000:
        valid_salaries[i] = valid_salaries[i] + (valid_salaries[i] * 0.05)
print("Salaries after Bonus:", valid_salaries)
# 3. Sort salaries in descending order
valid_salaries.sort(reverse=True)
print("Sorted Salaries (Descending):", valid_salaries)
# 4. Display top 3 highest salaries
top_3 = valid_salaries[:3]
print("Top 3 Highest Salaries:", top_3)