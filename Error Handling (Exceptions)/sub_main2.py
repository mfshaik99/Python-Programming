try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That wasn't a number.")
else:
    print("You entered:", number)
finally:
    print("This will always run, no matter what.")
