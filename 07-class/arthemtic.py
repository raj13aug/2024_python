class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return self.x + other.x, self.y + other.y 
    

point = Point(9,5)
other = Point(5,6)
combined = point + other   
print(combined)