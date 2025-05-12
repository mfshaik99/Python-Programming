# Decorators are used to modify the behavior of functions.

# Decorator to print function name
def decorator(func):
    def wrapper():
        print(f"Function {func.__name__} is being executed")
        return func()
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()  # Calls say_hello with the decorator
