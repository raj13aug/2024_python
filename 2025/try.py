while True:
    try:
        x = int(input("please enter the number "))
    except:
        print("whoop! There was some problem in code")    
    else:
        print(f"your value is {x}")
        break
    finally:
        print("All is well")