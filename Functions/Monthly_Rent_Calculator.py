# Function to calculate rent based on the type of house
def calculate_rent(house_type, area):
    rent_per_sqft = {"1BHK": 10, "2BHK": 15, "3BHK": 20}
    rent = rent_per_sqft.get(house_type, 0) * area
    return rent

# Input from the user
house_type = input("Enter the house type (1BHK, 2BHK, 3BHK): ")
area = float(input("Enter the area in square feet: "))

# Call the function
rent = calculate_rent(house_type, area)
print(f"The monthly rent for a {house_type} is: ${rent:.2f}")

