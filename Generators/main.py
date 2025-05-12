# Generators allow you to create iterators.

# Generator function to yield square of numbers
def square_generator(limit):
    for i in range(limit):
        yield i * i

gen = square_generator(5)

# Printing generator values
for value in gen:
    print(value)
