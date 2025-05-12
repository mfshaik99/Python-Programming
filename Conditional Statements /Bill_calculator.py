units = int(input("Enter electricity units used: "))

if units <= 100:
    cost = units * 2
elif units <= 200:
    cost = (100 * 2) + (units - 100) * 3
else:
    cost = (100 * 2) + (100 * 3) + (units - 200) * 5

print("Your bill amount is:", cost, "rupees")
