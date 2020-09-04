# Operator overloading

class Student:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __add__(self,other):
        return (self.a + other.a, self.b + other.b)
    
    def __gt__(self, other):
        if (self.a + self.b) > (other.a + other.b):
            return True
        else:
            return False


s1 = Student(32,3)
s2 = Student(33,3)
print(s1 + s2)
if s1 > s2:
    print('win')
else:
    print('wins')