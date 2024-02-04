class Car():
    count_of_wheels = 4
    
    def __init__(self, color, speed, mark):
        self.color = color
        self.speed = speed
        self.mark = mark
    
    def drive(self, place):
        print(f'The {self.color} {self.mark} car is driving to the {place} at the speed {self.speed} km/h')
    
my_car = Car('blue', 110, 'Toyota')

my_car.drive('KBTU')