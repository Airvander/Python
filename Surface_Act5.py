import math
r = float(input("Enter the Radius(units): "))
h = float(input("Enter the Height(units): "))

area = (2 * math.pi * r * h) + (2 * math.pi * r * r )
print("Surface Area =", area, "unit square")
