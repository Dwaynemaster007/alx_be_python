# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
# Note: The constant 32 is added/subtracted directly in the functions.

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius using the global factor.
    Formula: C = (F - 32) * 5/9

    Args:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature converted to Celsius.
    """
    # Accessing the global variable FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit using the global factor.
    Formula: F = (C * 9/5) + 32

    Args:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature converted to Fahrenheit.
    """
    # Accessing the global variable CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    """
    Handles user interaction, input validation, and displays the conversion result.
    """
    # 1. Get temperature input
    temp_input = input("Enter the temperature to convert: ").strip()

    # 2. Input Validation (Numeric Value)
    try:
        temperature = float(temp_input)
    except ValueError:
        # Raise the specified error message for non-numeric input
        print("Invalid temperature. Please enter a numeric value.")
        return # Exit the function if input is invalid

    # 3. Get unit input
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    # 4. Perform conversion and display result
    if unit == 'F':
        # Convert Fahrenheit to Celsius
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
    elif unit == 'C':
        # Convert Celsius to Fahrenheit
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
    else:
        # Invalid unit input
        print("Invalid unit specified. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()
