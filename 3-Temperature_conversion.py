

unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))
if unit.upper() == "C":
    temp = round((9 * temp) / 5 + 32)
    print(f"The temperature in Fahrenheit is {temp} F")
elif unit.upper() == "F":
    temp = round((temp -32) * 5 / 9)
    print(f"The temperature in Celsius is {temp} C")
else:
    print(f"{unit} was not valid")