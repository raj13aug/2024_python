def user_choice():
    # variables
    
    #Initial
    choice = 'Words'
    acceptables_range = range(0,10)
    within_range = False
    
    #Two condiditions to check
    #Digit  or within_range = False
    while choice.isdigit() == False or within_range == False:
        choice = input("please enter a number 0 to 10: ")
        
        if choice.isdigit() == False:
            print("Sorry is not digit")
            
        if choice.isdigit() == True:
             if int(choice) in acceptables_range:
                 within_range = True
             else:
                 print("you are out of out acceptables range")
                 within_range = False
            
    return int(choice)

user_choice()