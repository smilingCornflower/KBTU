class Car():
    count_of_wheels = 4
    
    def __init__(self, color, speed, mark):
        self.color = color
        self.speed = speed
        self.mark = mark
    
    def drive(self, place):
        print(f'The {self.color} {self.mark} car is driving to the {place} at the speed {self.speed} km/h')
    
class PoliceCar(Car):
    def __init__(self, color, speed, mark, blinker):
        super().__init__(color, speed, mark)
        self.blinker = blinker
    
    def drive(self, place):
        print(f'The {self.color} police car is driving to the {place} at the speed {self.speed} km/h')
        print('WEE WEE WEE')

official_car = PoliceCar('white', 130, 'Ford', True)

official_car.drive('Dostyk plaza')
