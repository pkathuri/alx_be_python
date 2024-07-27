# Class and Static methods in action
class Calculator:
    calculation_type = "Arithmetic Operations"
    # The static method in action
    @staticmethod
    def add(a,b):
        return a+b
    @classmethod
    def multiply(cls,a,b):
         print(f"Calculation type: {cls.calculation_type}")
         return a * b
         
