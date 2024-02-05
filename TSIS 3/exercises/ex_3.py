# Define a class named Rectangle which inherits from Shape class from task 2. 
# Class instance can be constructed by a length and width. 
# The Rectangle class has a method which can compute the area.

from ex_2 import Shape


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rectangle_obj = Rectangle(5, 3)
print("Area of Rectangle:", rectangle_obj.area())
