import math

# Input from user
r = float(input("Enter the radius of the cylinder: "))
h = float(input("Enter the height of the cylinder: "))

# Calculate curved surface area
curved_surface_area = 2 * math.pi * r * h

# Calculate total surface area
total_surface_area = 2 * math.pi * r * (r + h)

# Calculate volume
volume = math.pi * r**2 * h

# Display results
print("\nResults:")
print("Curved Surface Area =", round(curved_surface_area, 2))
print("Total Surface Area =", round(total_surface_area, 2))
print("Volume =", round(volume, 2))