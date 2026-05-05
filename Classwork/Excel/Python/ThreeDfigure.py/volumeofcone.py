import math

# Input from user
r = float(input("Enter the radius of the cone: "))
h = float(input("Enter the height of the cone: "))

# Calculate slant height
l = math.sqrt(r**2 + h**2)

# Calculate curved surface area
curved_surface_area = math.pi * r * l

# Calculate total surface area
total_surface_area = math.pi * r * (r + l)

# Calculate volume
volume = (1/3) * math.pi * r**2 * h

# Display results
print("\nResults:")
print("Slant Height =", round(l, 2))
print("Curved Surface Area =", round(curved_surface_area, 2))
print("Total Surface Area =", round(total_surface_area, 2))
print("Volume =", round(volume, 2))