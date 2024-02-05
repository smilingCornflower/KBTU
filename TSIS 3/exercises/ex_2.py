# Define a class named Shape and its subclass Square. 
# The Square class has an init function which takes a length as argument. 
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape:
    def area(self):
        return 0  # Дефольт

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2



shape_obj = Shape()
print("Area of shape:", shape_obj.area())

square_obj = Square(4)
print("Area of square:", square_obj.area())
