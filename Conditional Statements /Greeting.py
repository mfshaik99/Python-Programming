hour = int(input("Enter the hour (0-23): "))

if 5 <= hour < 12:
    print("Good Morning!")
elif 12 <= hour < 17:
    print("Good Afternoon!")
elif 17 <= hour < 21:
    print("Good Evening!")
else:
    print("Good Night!")
