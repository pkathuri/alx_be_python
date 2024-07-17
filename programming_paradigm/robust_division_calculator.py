def safe_divide(numerator,denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        if numerator == 0:
            return "Error: Cannot divide by zero."
        else:
            return result
    except ValueError:
        print("Enter numeric values only")

result = safe_divide(1,2)
print(result)
        
