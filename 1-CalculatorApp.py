#Python calculator
operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter a first number: "))
num2 = float(input("Enter a second number: "))
if operator == "+":
    result = num1+ num2
    print(round(result))
elif operator == "-":
    result = num1- num2
    print(round(result))
elif operator == "*":
    result = num1* num2
    print(round(result))
elif operator == "/":
    result = num1/num2
    print(round(result))
else:
    print(f"{operator} is not valid! ")



