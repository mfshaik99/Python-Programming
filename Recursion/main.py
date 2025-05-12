# A function calling itself is called Recursion

# Recursive function to calculate factorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")  # 120
