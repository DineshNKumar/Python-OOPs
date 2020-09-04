from abc import ABC, abstractmethod

#Abstract class and interfaces


class Computer(ABC):  # interface and abstract class
    @abstractmethod   # abstract method
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print('Running')
        
class Programmer:
    def work(self, com):
        print('Solving bugs')
        com.process()

class Whiteboard:
    def write(self):
        print('It is writing')
        
if __name__ == '__main__':
    laptop = Laptop()
    programmer = Programmer()
    programmer.work(laptop)
   
    
    
    