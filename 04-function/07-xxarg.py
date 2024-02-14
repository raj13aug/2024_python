def value(**argsq):
    print(argsq)
    
value(id='raj', name = 'raj')


def value(**argsq):
    print(argsq["id"])
    
value(id='raj', name = 'raj')
