def perform_operation(num1:float,num2:float,operation:str):
    match operation:
        case operation == "add":
            return num1 + num2
        case operation == "subtract":
            return num1 - num2
        case operation == "multiply":
            return num1*num2
        case operation == "divide":
            if num2 !=0:
                return num1 / num2
            else:
                return "zero division error"

result = perform_operation(10.2,5.1,"divide")
print(result)

