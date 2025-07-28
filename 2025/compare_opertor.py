class Compare():
    
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        
    def __str__(self):
        return self.y
    
    def __eq__(self):
        return self.x == self.y
    
point = Compare(5,5)
print(point)