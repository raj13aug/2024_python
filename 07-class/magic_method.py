class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"{self.x},{self.y}"
    

point = Point(9,5)    
print(point)
