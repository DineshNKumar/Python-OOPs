class Cars:
    def __init__(self, speed, color):
        self.__speed = speed
        self.__color = color
    
    def set_speed(self, speed):
        self.__speed = speed
    
    def get_speed(self):
        return self.__speed
    
    def set_color(self, color):
        self.__color = color
    
    def get_color(self):
        return self.__color

if __name__ == "__main__":
    car = Cars(213, "Yellow")
    print(car.get_color())

    car.__color = "G"
    print(car.get_color())
    


