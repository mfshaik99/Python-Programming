#Working with files in Python.
# File Handling
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a test file.")

# Reading from the file
with open("example.txt", "r") as file:
    content = file.read()
    print(f"File content: {content}")
