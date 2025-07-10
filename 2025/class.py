# class Sleep:
#     vars = "Are you sleeping"
    
#     def __init__(self, name, age):
#         self.name = name
#         self.name = age
        
#     def hello():
#         pass
    

# nan = Sleep(name="raj", age=36)

class Circle:
    pi = 3.14
    
    def __init__(self, radius=3):
        self.radius = radius
        self.area = radius * radius * Circle.pi
        
    def setRadius(self, new_radius=5):
        self.radius = new_radius
        self.area =  new_radius * new_radius * self.pi
        
    def getCircumference(self):
        return self.radius * self.pi * 2
    
c =  Circle()
print('radius is ', c.radius)        
print('Area is', c.area)
print('circumference is:', c.getCircumference())
