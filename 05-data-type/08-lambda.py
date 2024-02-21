items = [
    ("product1", 10),
    ("product2", 40),
    ("product3", 30),
]



items.sort(key=lambda item:item[1])
print(items)