class Cars:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color
    
    def set_speed(self, speed):
        self.speed = speed
    
    def get_speed(self):
        return self.speed
    
    def set_color(self, color):
        self.color = color
    
    def get_color(self):
        return self.color

car = Cars(222, 'Green')

print(car.get_speed())

car.speed = 234

print(car.get_color())
car.set_speed(322)
print(car.get_speed())

