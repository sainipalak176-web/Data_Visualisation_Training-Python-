
# List of triangle sides to test
triangles = [
    (3, 3, 3),   # Equilateral
    (5, 5, 8),   # Isosceles
    (3, 4, 5),   # Scalene
    (2, 2, 5)    # Invalid triangle
]

for sides in triangles:
    a, b, c = sides
    if a + b > c and a + c > b and b + c > a:  # Triangle validity check
        if a == b == c:
            t_type = "Equilateral"
        elif a == b or b == c or a == c:
            t_type = "Isosceles"
        else:
            t_type = "Scalene"
        print(f"Problem 17 - Sides {sides} form a {t_type} triangle")
    else:
        print(f"Problem 17 - Sides {sides} do not form a valid triangle")

# Output inside code:
# Problem 17 - Sides (3, 3, 3) form a Equilateral triangle
# Problem 17 - Sides (5, 5, 8) form a Isosceles triangle
# Problem 17 - Sides (3, 4, 5) form a Scalene triangle
# Problem 17 - Sides (2, 2, 5) do not form a valid triangle