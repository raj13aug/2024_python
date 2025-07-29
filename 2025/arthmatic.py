class Point:
    def __init__(self, x ,y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
        #return self.x + other.x, self.y + other.y
    
    def __str__(self):
        return f"Point {self.x}, {self.y}"
    
value = Point(5,5)
other1 = Point(10, 10)  
print(value + other1)