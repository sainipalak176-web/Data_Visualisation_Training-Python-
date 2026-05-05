#check whether a given year is a leap year.
# Test years
years = [2000, 1900]

for year in years:
    # Leap year condition
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f" {year} is a Leap Year")
    else:
        print(f" {year} is Not a Leap Year")


#output:
"""2000 is a leap year"""
"""1900is not a leap year"""

