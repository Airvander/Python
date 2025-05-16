import math

radius = float(input(" Enter radius(units):"))
height = float(input(" Enter height(units):"))


area = (2 * math.pi * radius * height) + (2 * math.pi * radius **2)

print("Surface area =", area,"units square" )
