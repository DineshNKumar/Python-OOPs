class A:
    
    def __init__(self):
        print('A is init')
        
    def features1(self):
        print('Feature one')
    
    def features2(self):
        print('Feature two')

class B:
    def __init__(self):
        print('B is init')
    
    def features3(self):
        print('Feature three')
    
    def features4(self):
        print('Feature four')

class C(A,B):
    def __init__(self):
        super().__init__()
        print('C is init')
    
    def features5(self):
        super().features1()
        super().features3()
        
c = C()
c.features5()
