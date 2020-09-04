class Student:
    
    school = 'Sanskriti University'
    
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    
    @classmethod
    def info(cls):
        return cls.school
    
    @staticmethod
    def info1():
        print('Hello world in the class')

if __name__=='__main__':
    s1 = Student(2,1,4)
    s2 = Student(4,6,1)
    print(s1.avg())
    print(s2.avg())
    print(Student.info())
    Student.info1()
    