class Car():
    count_of_wheels = 4
    
    def __init__(self, color, speed, mark):
        self.color = color
        self.speed = speed
        self.mark = mark
    

    
my_car = Car('blue', 110, 'Toyota')
print(f"I have a {my_car.color} {my_car.mark} car, which max speed is {my_car.speed} km/h")
