# def chec_even_list(num_list):
#     for number in num_list:
#         if num_list == True:
#             return True
#     else:
#         pass
    
#     return False

# var = chec_even_list([1,2,3,4])
# # print(var)


def even_number(even1):
    even_number = []
    for number in even1:
        if number % 2 == 0:
             even_number.append(number)
    else:
        pass
    return even_number


print(even_number([1, 2, 3, 4, 5]))