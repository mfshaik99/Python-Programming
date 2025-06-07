try:
    file = open("example.txt", "r")
    content = file.read()
    print("File content:\n", content)
except FileNotFoundError:
    print("Error: The file was not found.")
finally:
    # This will run no matter what (even if an error happens)
    try:
        file.close()
        print("File has been closed.")
    except NameError:
        # In case file was never opened
        print("No file was opened, so nothing to close.")
