# method overloading

class Cal:    
    def sum(self,a, b):
        return a + b
    
    def sum(self, a=0, b=0, c=0):
        return a + b + c


c = Cal()
print(c.sum(12,12,12))
print(c.sum(3,2))
print(c.sum(2))
