class Point:
    var = "Yellow"
    
    def __init__(self,x,y):
        self.x = x
        self.y = y

point = Point(1,3)
print(point.var)