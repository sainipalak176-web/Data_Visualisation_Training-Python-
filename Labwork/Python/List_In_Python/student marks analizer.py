# Student Marks Analyzer
marks = [78, 95, 102, -5, 88, 67, 95, 45]
# 1. Remove invalid marks
valid_marks = []
for m in marks:
    if 0 <= m <= 100:
        valid_marks.append(m)
print("Valid Marks:", valid_marks)
# 2. Calculate average
average = sum(valid_marks) / len(valid_marks)
print("Average Marks:", average)
# 3. Find topper(s)
highest = max(valid_marks)
toppers = []
for m in valid_marks:
    if m == highest:
        toppers.append(m)
print("Topper Marks:", toppers)
# 4. Display grade based on average
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)
