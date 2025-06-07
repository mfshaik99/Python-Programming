try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print("Result:", result)
except ValueError:
    print("Please enter only numbers.")
except ZeroDivisionError:
    print("You can't divide by zero!")
