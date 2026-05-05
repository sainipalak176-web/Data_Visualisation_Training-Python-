#calculate bmi
# List of test data: (weight in kg, height in meters)
bmi_data = [
    (50, 1.6),
    (68, 1.7),
    (85, 1.75),
    (95, 1.65)
]

for weight, height in bmi_data:
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    print(f"Problem 18 - Weight: {weight}kg, Height: {height}m -> BMI: {round(bmi,2)}, Category: {category}")

# Output inside code:
# Problem 18 - Weight: 50kg, Height: 1.6m -> BMI: 19.53, Category: Normal weight
# Problem 18 - Weight: 68kg, Height: 1.7m -> BMI: 23.53, Category: Normal weight
# Problem 18 - Weight: 85kg, Height: 1.75m -> BMI: 27.76, Category: Overweight
# Problem 18 - Weight: 95kg, Height: 1.65m -> BMI: 34.9, Category: Obese