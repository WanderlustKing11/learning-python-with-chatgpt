# Lesson 2
# Control Structures

# These allow us to direct the flow of our program
# based on conditions and loops

# if, elif, and else statements

# These are conditional statements used to execute
# different blocks of code based on certain conditions.

x = 10
y = 20


if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x and y are equal")


# Loops
    
# Python has two primary types of loops:
# `for` and `while`.
    
# For Loop: Used for iterating over a sequence
# (like a list, tuple, dictionary, set, or string).
    
# Iterating over a range
print("'for' loop range")
for i in range(5):  # Will loop from 0 to 4
    print(i)

# Iterating over a list
print("'for' loop list")
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)


# While Loop: Executes a set of statements as long
# as a condition is true.

print("Using 'while' loop:")
count = 0
while count < 5:
    print(count)
    count += 1  # This is equivalent to count = count + 1


# Controling Loop Execution:
# 'break': Exits the loop.
# 'continue': Skips the rest of the loop's body
#             and goes to the next iteration.

# Using break
print("Learning 'break':")
for i in range(10):
    if i == 5:
        break
    print(i)

# Using continue
print("Learning 'continue':")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)    # This will print only odd numbers


