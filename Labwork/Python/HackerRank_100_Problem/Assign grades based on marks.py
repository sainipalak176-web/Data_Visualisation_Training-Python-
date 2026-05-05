#assign grades based on marks.
# List of student marks
marks_list = [95, 82, 67,50,35]

for marks in marks_list:
    if marks >= 90:
        grade = 'A+'
    elif marks >= 80:
        grade = 'A'
    elif marks >= 70:
        grade = 'B+'
    elif marks >= 60:
        grade = 'B'
    elif marks >= 50:
        grade = 'C'
    elif marks >= 35:
        grade = 'D'
    else:
        grade = 'F'
    print(f"Problem 12 - Marks: {marks}, Grade: {grade}")

# Output :
""" Marks: 95, Grade: A+"""
""" Marks: 82, Grade: A"""
""" Marks: 67, Grade: B"""
""" Marks: 50, Grade: C"""
""" Marks: 35, Grade: D"""

