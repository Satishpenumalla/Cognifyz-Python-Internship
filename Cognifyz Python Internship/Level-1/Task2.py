temperature, unit = input("Enter the temperature and unit of measurement 'C' for Celsius and 'F' for fahrenheit : ").split()
unit = unit.upper()
if unit == 'C':
    fahrenheit = (9/5)*float(temperature) + 32
    print(f"The temperature converted to Fahrenheit is {round(fahrenheit,2)}°F")

elif unit == 'F':
    celsius = (5/9)*(float(temperature)-32)
    print(f"The temperature converted to Celsius is {round(celsius,2)}°C")

else:
    print("Entre a valid temperature reading or valid unit of measurement")