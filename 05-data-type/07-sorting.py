items = [
    ("product1", 10),
    ("product2", 40),
    ("product3", 30),
]

def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)


number = [1,2,3,4,6,5]

number.sort()
print(number)
