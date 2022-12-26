
operator = input("Enter and operator (+ - * /):")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2st number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 20))
elif operator == "-":
    result = num1 - num2
    print(round(result, 20))
elif operator == "*":
    result = num1 * num2
    print(round(result, 20))
elif operator == "/":
    result = num1 / num2
    print(round(result, 20))
else:
    print(f"{operator} is not a valid operator")


