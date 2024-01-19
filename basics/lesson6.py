# Lesson 6
# Error Handling

#In Python, errors are caught and handled using 
# try and except blocks. This prevents the program 
# from crashing and allows you to deal with 
# unexpected situations gracefully.

# Basic Try-Except Block
# The simplest form of error handling is a 
# try-except block. 

try:
    # Code that may cause an error
    result = 10 / 0
except ZeroDivisionError:
    # What to do if the error occurs
    print("Divided by zero!")

# Catching Multiple Exceptions

try:
    # Code that may cause different errors
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Divided by zero!")


# Finally Block
# The finally block is optional and used for 
# code that should run no matter what, like cleaning 
# up resources (e.g., closing files).

try:
    f = open("example.txt")
    # process file
except FileNotFoundError:
    print("File not found.")
finally:
    f.close()


# Raising Exceptions
# You can also 'raise' exceptions in Python, 
# forcing an error to occur when certain conditions 
# are met.
    
x = -1
if x < 0:
    raise ValueError("x should not be negative")


