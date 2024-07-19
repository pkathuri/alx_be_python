FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# A function that takes in temperature in Fahreinheit and converts to Celcius
def convert_to_celcius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# A function that converts celciys to Fahreinheit

def convert_to_fahreiheit(celcius):
     return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
   while True:
       try:
            temperature = float(input("Enter the temperature to convert:"))
            units = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
            if units.upper() == "C":
               results = convert_to_fahreiheit(temperature)
               units_of_conversion = "F"
            elif units.upper() == "F":
                results = convert_to_celcius(temperature)
                units_of_conversion = "C"
            else:
                raise ValueError("Invalid input of temperature units, insert C/F")
            print(f'{temperature} {units} is {results} {units_of_conversion}.')
       except:
        #    print(e)
           raise ValueError("Invalid temperature, insert a numeric value.")
