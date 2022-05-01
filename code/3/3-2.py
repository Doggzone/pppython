from math import pi

def area_circle(radius, n):
    area = pi * radius ** 2
    return round(area, n)

print(area_circle(3, 1))
print(area_circle(-3, 1))