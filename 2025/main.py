#how to call mutiple files in single file?

def add(x,y):
    print(x + y)
    
def mul(x, y):
    print(x * y)

print(__name__)    
if __name__ == "__main__":
    mul(7,5)
    add(7,8)
        