num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")
match operation:
    case "*":
        product = num1 * num2
        print(f"The result is {product}")
    case  "+":
        sum_=num1+num2
        print(f"The result is {sum_}")
    case "-":
        difference = num1 - num2
        print(f"The result is {difference}")
    case "/":
        if num2 != 0:
            division = num1/num2
            print(f"The result is {division}")
        else:
            print("Cannot divide by zero")            
    case _:
        print("The result is invalid")
