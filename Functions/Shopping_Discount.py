# Function to calculate total cost with discount
def calculate_total(cart, discount=0):
    total = sum(cart)
    discounted_price = total - (total * discount / 100)
    return discounted_price

# Input for shopping cart
cart = []
items = int(input("How many items did you buy? "))
for i in range(items):
    price = float(input(f"Enter price for item {i + 1}: "))
    cart.append(price)

# Optional discount input
discount = float(input("Enter discount percentage (0 if none): "))

# Call the function
total_price = calculate_total(cart, discount)
print(f"Total cost after discount: ${total_price:.2f}")
