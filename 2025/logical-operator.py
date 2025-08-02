loan_eliglibe = True
loan_non_eliglibe = False
student = False

if (loan_eliglibe or loan_non_eliglibe) and not student:
    print("eligible")
else:
    print("non eligible")    
    
#note : In python logical opertor are short circuit    


age = 28

if 22 <= age < 65:
    print("chain of operator")