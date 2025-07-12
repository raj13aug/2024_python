
class Life_lesson():
    
    def __init__(self,book,author,page):
        self.book = book
        self.author = author
        self.page = page
        
    def __str__(self):
        return f"hello, this is {self.author} and my book name is {self.book}"
        
    def __len__(self):
        return self.page
        

b = Life_lesson("owncompanybuild","Nataraj",300)        

print(str(b))
print(len(b))
        
class LifeLesson:
    
    def __init__(self, book, author, page):
        self.book = book
        self.author = author
        self.page = page
        
    def __str__(self):
        return f"Hello, this is {self.author} and my book name is {self.book}"
        
    def __len__(self):
        return self.page  # Should return an int, not a string
        

b = LifeLesson("owncompanybuild", "Nataraj", 300)        

print(str(b))   # Displays the string representation
print(len(b))   # Displays the length (number of pages)
        