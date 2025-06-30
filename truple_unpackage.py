def employee_check(working_hour):
    current_max = 0
    employee_month = ''
    
    for employee,hours in working_hour:
        if hours > current_max:
            current_max = hours
            employee_month = employee
        else:
            pass
    
    return (employee_month, current_max)

working_hour = [("ravi",100),("rama", 300), ("mano",500), ("nat", 200)]
result = employee_check(working_hour)
print(result)