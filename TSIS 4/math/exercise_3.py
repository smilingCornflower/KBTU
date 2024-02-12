from math import tan, pi

# Write a Python program to calculate the area of regular polygon.
# Input number of sides: 4
# Input the length of a side: 25
# The area of the polygon is: 625

def get_polygon_area(sides_amount, side_length):
    perimeter = sides_amount * side_length
    apothem = side_length / (2 * tan(pi / sides_amount))
    return round(perimeter * apothem / 2, 3)


print(get_polygon_area(4, 25))
    