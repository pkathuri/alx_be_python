def perform_operation(num1:float,num2:float,operation:str):
    if operation == 'add':
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
           return "Zero division error"
    else:
        return "invalid operation"  
result = perform_operation(10.5,5.5,"divide")
print(result)
    
