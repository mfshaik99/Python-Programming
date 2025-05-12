age = int(input("Enter your age: "))

if age <= 5:
    print("You can travel for free.")
elif age <= 18:
    print("You get a child discount fare.")
elif age >= 60:
    print("You get a senior citizen discount.")
else:
    print("You must pay the full fare.")
