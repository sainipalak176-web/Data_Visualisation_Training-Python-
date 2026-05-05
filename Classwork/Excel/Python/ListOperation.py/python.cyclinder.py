import math
radius=float(input("enter the radius of cyclinder:"))
height=float(input("enter the height of the cyclinder:"))
csa=2*math.pi*radius*height
tsa=2*math.pi*radius*(radius+height)
volume=math.pi*radius**2*height
#displaying results
print(f"curves surafce area :{csa:.2f}")
print(f"total surface area:{tsa:.2f}")
print(f"volume of cyclinder{volume:.2f}")