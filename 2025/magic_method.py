# class Happy:
    
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __str__(self):
#         return f"add both number {self.x}, {self.y}"
    
#     def add(self):
#         print(f"add both number {self.x}, {self.y}")
        
# point = Happy(9,0)        
# point()


class Happy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Object with values x={self.x}, y={self.y}"

    def add(self):
        return self.x + self.y

# Create an instance of Happy
point = Happy(9, 0)

# Call the add method
print(f"Sum of both numbers: {point.add()}")

# Print the object (which uses the __str__ method)
print(point)
