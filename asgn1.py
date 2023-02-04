# Assignment - 1
# To calculate the area of triangle, circle & a square.

import math

print("For traingle:-")
base = float(input("Enter the base: "))
height = float(input("Enter the height: "))
areaOfTriangle = 0.5*base*height

print("For Circle:-")
radius = float(input("Enter the radius: "))
areaOfCircle = math.pi*radius*radius

print("For Square:-")
side = float(input("Enter the side: "))
areaOfSquare = side*side

print(f"Area of triangle = {areaOfTriangle} sq. units")
print(f"Area of circle = {areaOfCircle:.2f} sq. units")
print(f"Area of square = {areaOfSquare} sq. units")