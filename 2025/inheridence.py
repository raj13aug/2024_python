#inheridence

class Animal():
    def __init__(self):
        print("Animal is created")
        
    def WhoAMI(self):
        print("eating")
        
    def eat(self):
        print('Eating')
        
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
        
    def WhoAMI(self):
        print('dog')
        
    def bark(self):
        print("woof!")     
        
d = Dog()        
d.WhoAMI()        