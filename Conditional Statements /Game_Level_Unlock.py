score = int(input("Enter your game score: "))

if score >= 100:
    print("Level 3 Unlocked!")
elif score >= 50:
    print("Level 2 Unlocked!")
else:
    print("Try again to unlock next level.")
