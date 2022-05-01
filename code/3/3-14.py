from math import pi

def area_circle(radius, n):
    if radius > 0:
        area = pi * radius ** 2
        return round(area, n)
    else:
        return 0.0

print("Circle Area Calculator")
more = 'y'
while more == 'y':
    r = input("Radius? ")
    while not r.isdigit():
        r = input("Radius? ")
    p = input("Precision? ")
    while not p.isdigit():
        p = input("Precision? ")
    area = area_circle(int(r),int(p))
    print("The area of a circle with radius", r, "is", area, ".")
    more = input("Press y to continue, any other key to exit. ")
print("Please come back again.")