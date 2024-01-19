# Lesson 3
# Data Structures

# Python has several built-in data structures 
# that are commonly used. We'll focus on Lists, 
# Dictionaries, Tuples, and Sets.


# Lists
# Lists are ordered and mutable (changeable) 
# collections that can hold a mix of data types.

# Creating a list
my_list = [1, 2, 3, "Python", 5.5]

# Accessing list elements
print(my_list[0])       # prints 1
print(my_list[-1])      # prints 5.5 (last element)

# List operations
my_list.append('new item')  # Adds an item to the end
my_list[2] = 'three'        # Changes the element at index 2

# Slicing
print(my_list[1:4])     # Gets items from index 1 to 3

# Dictionaries
# Dictionaries are unordered, changeable, 
# and indexed collections. They have keys and values.

# Creating a dictionary
my_dict = {"name": "Doug", "age": 36, "city": "New York"}

# Accessing dictionary values
print(my_dict['name'])  # prints 'Doug'

# Adding new key-value pair
my_dict["email"] = "doug@example.com"
print(my_dict)

# Changing a value
my_dict["age"] = 37
print("My new age: ", my_dict["age"])

# Tuples
# Tuples are ordered and immutable (cannot be 
# changed). They are similar to lists but are 
# defined with parentheses.

# Creating a tuple
my_tuple = (1, 2, 3, 'Python')

# Accessing tuple elements
print("3rd tuple element:", my_tuple[2])  # prints 3

# Sets
# Sets are unordered, unindexed collections with 
# no duplicate elements. They're great for 
# membership testing and eliminating duplicate 
# entries.

# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding an item to a set
my_set.add(6)

# Removing an item
my_set.remove(3)

# Checking membership
print(2 in my_set)  # prints true

print("Current set:", my_set)