number = [1,2,3,4,5,6]

def mapp(numbers):
    return numbers * 2


result = map(mapp, number)
print(list(result))