def perform_operation(num1,num2,operation):
    match operation:
        case "+":
            sum = num1 + num2
            return sum
        case "-":
            difference = num1 - num2
            return difference
        case "*":
            product = num1 * num2
            return product
        case "/":
            if num2 !=0:
               division = num1 / num2
            else:
                return "error"
        case _:
            return "invalid"
                
