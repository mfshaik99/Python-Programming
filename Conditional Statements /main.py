# Sample conditions
condition1 = True
condition2 = False
condition3 = 10 > 5  # Just an example condition
condition4 = 5 == 5   # Just another example condition

# if condition: (simple if statement)
if condition1:
    print("Condition1 is True.")

# if-else statement
if condition2:
    print("Condition2 is True.")
else:
    print("Condition2 is False.")

# Nested if-else statement
if condition1:
    if condition2:
        print("Both condition1 and condition2 are True.")
    else:
        print("condition1 is True, but condition2 is False.")
else:
    print("condition1 is False.")

# if with logical 'and'
if condition1 and condition2:
    print("Both condition1 and condition2 are True.")

# if with logical 'or'
if condition1 or condition2:
    print("At least one of condition1 or condition2 is True.")

# if-elif-else chain
if condition3:
    print("Condition3 is True.")
elif condition4:
    print("Condition3 is False, but condition4 is True.")
else:
    print("Both condition3 and condition4 are False.")

# if with 'not' operator
if not condition2:
    print("Condition2 is False (checked with 'not').")
