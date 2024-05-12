class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    

point = Point(9,5)
other =Point(9,6)
print(point == other)