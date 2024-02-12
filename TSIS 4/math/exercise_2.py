# Write a Python program to calculate the area of a trapezoid.
# Height: 5
# Base, first value: 5
# Base, second value: 6
# Expected Output: 27.5


def get_trapezoid_area(a=1, b=1, h=1):
    return (a + b) * h / 2

print(get_trapezoid_area(5, 5, 6))