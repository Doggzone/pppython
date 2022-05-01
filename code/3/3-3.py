from math import pi

def area_circle(radius, n):
    if radius > 0:
        area = pi * radius ** 2
        return round(area, n)
    else:
        return 0.0

print(area_circle(3, 1))
print(area_circle(-3, 1))