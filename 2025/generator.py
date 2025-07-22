def muli(no):
    for i in range(no):
        yield no ** 3

      
for num in muli(9):
    print(num)