class Computer:
    
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
    
    def config(self):
        print('CPU -', self.cpu, ' Ram - ', self.ram)

class Computer1:
    
    def __init__(self):
        self.name = 'Dinesh'
        self.age = 32
    
    def update(self):
        self.age = 34
    
    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False
    
    

if __name__ == '__main__':
    comp1 = Computer('5i', 6)
    comp1.config()
    
    c1 = Computer1()
    c2 = Computer1()
    c1.age = 30
    if c1.compare(c2):
        print('Same')
    else:
        print('Different')
    