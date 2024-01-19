# Lesson 4
# Functions

# In Python, you use the def keyword to 
# define a function.

# Defining a function
def greet(name):
    print(f"Hello, {name}!")

# Calling the function
greet("Doug")

# Return Values
# Functions can return values using the 
# return keyword. 

def add(x, y):
    return x + y

# Calling the function and printing its return value
result = add(5, 6)
print("Sum is:", result)

# Scope of Variables
# Variables defined inside a function are not 
# accessible outside of it. These are called 
# local variables. However, a function can access 
# variables defined outside of it, which are known 
# as global variables.

# Global variable
x = "global"

def demo_function():
    # Local variable
    y = "local"
    print(x)  # This will print 'global'
    print(y)  # This will print 'local'

demo_function()

# Trying to access local variable outside the
# function will raise an error

# print(y)  # This will cause an error

# Default Argument Values
# You can provide default values for function 
# arguments. If a value for that argument 
# is not passed when the function is called, 
# the default value is used.

# Function with default argument
def greet(name="World"):
    print(f"Hello, {name}!")

greet()         # Will print "Hello, World!"
greet("Doug")   # Will print "Hello, Doug!"

# Keyword Arguments
# When calling functions, you can specify 
# arguments by their names, which allows you 
# to pass arguments in any order.

# Function with two arguments
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

# Calling function with keyword arguments
display_info(age=30, name="Bob")