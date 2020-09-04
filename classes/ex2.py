import pandas

class Car:
    wheels = 4
    
    def __init__(self):
        self.mil = 10
        self.car = 'BMW'

if __name__=='__main__':
    car1 = Car()
    car2 = Car()
    print(car1.mil, car1.car, Car.wheels)
    print(pandas.__version__)
    