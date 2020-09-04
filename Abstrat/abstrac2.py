from abc import ABC,abstractmethod
import math


class Shape(ABC):
    r = 0
    def __init__(self, r):
        self.r = r 
    
    @abstractmethod
    def area(self):
        pass
    
    def radius(self):
        pass


class Circle(Shape):
    def area(self):
        return 2 * math.pi * self.r * self.r 
    
    def radius(self):
        return self.r 

if __name__ == '__main__':
    ab = Circle(3)
    print(ab.area())
    print(ab.radius())
    