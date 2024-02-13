import math
import unittest

def calc_circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be either int or float")

    if not radius > 0:
        raise ValueError("Radius must be a positive integer")

    area = math.pi * radius ** 2

    return area


radius = input("Enter the radius:")

print(f"The area of the circle :{calc_circle_area(int(radius))}")



