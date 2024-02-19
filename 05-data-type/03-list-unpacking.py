number = [1,3,4,5,6,76,9]

first, second, *thrid = number
print(first)
print(second)
print(thrid)


first, *second, last = number
print(first, last, second)