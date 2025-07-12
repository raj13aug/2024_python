
class Car():
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("Drive")
        
class Boat():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("sail")
        
class Plane():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("fly")    
        
car = Car("ford","figo")        
boat = Boat("natar","steam board")
fly = Plane("Boeing", "747")


for i in (car,boat,fly):
    i.move()
    
    
    
    
        
        