x = 'global'

def outer():
    x = 'enclosing'
    print(x)
    def inner():
        x = 'local'
        print(x)  # Looks in L → E → G → B
    inner()

outer()
print(x)

#############################################################
x = 10  # Global variable

def change_global():
    global x
    x = 20  # Modifies the global variable

change_global()
print(x)  # Output: 20



#####################################

def outer():
    x = "outer value"

    def inner():
        nonlocal x
        x = "modified by inner"

    inner()
    print(x)

outer()
# Output: modified by inner
