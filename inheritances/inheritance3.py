class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
    
    def show(self):
        print(self.name, self.rollno)
        self.lap.show()
    
    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.ram = '2GM'
            self.cpu = 'AMD'
        
        def show(self):
            print(self.brand, self.ram, self.cpu)


if __name__=='__main__':
    outer = Student('Dinesh',19202033)
    outer.show()