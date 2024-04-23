# def multiply(*numbers):
#     print(numbers)
    
# multiply(8,8,8,8)


# def multiply(*numbers):
#     for n in numbers:
#         print(n)
        
# multiply(3,4,6,7)

# def mutiply(*numbers):
#     total = 1
#     for n in numbers:
#         total *= n
#     return total

# print(mutiply(2,3,4,5))


def total(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(total(2,3,4,5))