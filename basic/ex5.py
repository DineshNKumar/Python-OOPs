#Inheritance

class A:
    def features1(self):
        print('Feature one')
    
    def features2(self):
        print('Feature two')

class B(A):     # multilevel  
    def features3(self):
        print('Feature three')
    
    def features4(self):
        print('Feature four')

class C(B,A): # multiple 
    def features5(self):
        print('Feature five')
    
    def features6(self):
        print('Feature six')

if __name__ =='__main__':
    b = B()
    b.features1()
    b.features4()
    
    c = C()
    c.features1()
    c.features3()

    
    
    
    
    
    
    
    
    