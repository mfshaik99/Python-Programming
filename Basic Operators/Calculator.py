# Get two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Ask user to choose an operation
print("Choose an operation: +, -, *, /, %, **")
operator = input("Enter operator: ")

# Perform calculation based on operator
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
elif operator == "%":
    result = num1 % num2
elif operator == "**":
    result = num1 ** num2
else:
    result = "Invalid operator"

# Show the result
print("Result:", result)
