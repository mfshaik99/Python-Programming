# Catching and handling exceptions

# Error Handling
try:
    num = int(input("Enter a number: "))  # If user enters a non-number, it'll raise an error
    print(f"Number is {num}")
except ValueError:
    print("That's not a valid number!")
