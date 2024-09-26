FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR  # Convert F to C

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32  # Convert C to F

def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))  # Get user input
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()  # Get unit input

        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)  # Convert to Celsius
            print(f"{temperature}°F is {converted_temp}°C")
        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)  # Convert to Fahrenheit
            print(f"{temperature}°C is {converted_temp}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")  # Handle invalid numeric input

if __name__ == "__main__":
    main()  
