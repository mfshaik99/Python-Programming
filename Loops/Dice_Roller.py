import random

rolls = int(input("How many times would you like to roll the dice? "))

for i in range(rolls):
    dice_roll = random.randint(1, 6)
    print(f"Roll {i + 1}: {dice_roll}")
