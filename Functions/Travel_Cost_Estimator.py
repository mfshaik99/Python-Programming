# Function to calculate travel cost based on distance and vehicle type
def calculate_travel_cost(distance, vehicle_type):
    rates = {"car": 0.5, "bus": 0.2, "bike": 0.1}
    cost = distance * rates.get(vehicle_type, 0)
    return cost

# Input for travel details
distance = float(input("Enter the travel distance in kilometers: "))
vehicle_type = input("Enter the vehicle type (car, bus, bike): ")

# Call the function
cost = calculate_travel_cost(distance, vehicle_type)
print(f"Your travel cost is: ${cost:.2f}")
