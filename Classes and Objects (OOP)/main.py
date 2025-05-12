# Object-Oriented Programming in Python.

# Class and Object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Creating an object of the Person class
person1 = Person("Alice", 25)

# Calling a method
print(person1.greet())
