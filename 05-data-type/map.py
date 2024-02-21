items = [
    ("product1", 10),
    ("product2", 40),
    ("product3", 30),
]

value = []

for item in items:
    value.append(item[1])
    
print(value)


x = list(map(lambda item: item[1], items))
print(x)