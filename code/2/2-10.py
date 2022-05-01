# Calculate the area of circle 
# in: radius from standard input
# out: area of circle to standard output
radius = float(input("Enter the radius: "))
from math import pi
area = pi * radius ** 2 # calculate the area of circle
print("The area of a circle with radius", radius, "is", area)