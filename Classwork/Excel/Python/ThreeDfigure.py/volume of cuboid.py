# Program to calculate CSA, TSA and Volume of a cuboid

# Taking input from user
length = float(input("Enter length of cuboid: "))
breadth = float(input("Enter breadth of cuboid: "))
height = float(input("Enter height of cuboid: "))

# Calculations
curved_surface_area = 2 * height * (length + breadth)
total_surface_area = 2 * (length * breadth + breadth * height + height * length)
volume = length * breadth * height

# Display results
print("Curved Surface Area of cuboid:", curved_surface_area)
print("Total Surface Area of cuboid:", total_surface_area)
print("Volume of cuboid:", volume)