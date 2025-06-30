def argruments(*args):
    print(args)
    print("I love my egg {}".format(args[0]))
    
def dicts(**kwargs):
    print(kwargs)
    print("I love my fruit called {}".format(kwargs['food']))
    
args = argruments(10,23,5,8,6,7)
dicts1 = dicts(food="apple")
    
    
    
    
