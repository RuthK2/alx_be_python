FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return(celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

try:
    temp_input = input("Enter the temperature to convert: ")
    temperature = float(temp_input)
    unit = input("Is this in Celsius (C) or Farenheit (F)? ").strip().upper()
    if unit == 'F':
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted:.1f}°C")
    elif unit =='C':
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted:.1f}°F")
    else:
       raise ValueError("Invalid unit.Please enter 'C' or 'F'.")
except ValueError:
    print("Invalid temperature.Please enter a numeric value.")

