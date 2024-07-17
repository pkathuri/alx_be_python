def safe_divide(numerator,denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        if denominator == 0:
            return "Error: Cannot divide by zero."
        else:
            return result
    except ValueError:
        return "Enter numeric values only"
        
