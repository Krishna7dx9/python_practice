# ------------------------------------------------------------
# DATA TYPES IN PYTHON — FULL EXPLANATION + PRACTICE
# ------------------------------------------------------------

# Python has 7 MAIN built-in data types:
# 1. int          → whole numbers (10, -5, 0)
# 2. float        → decimal numbers (3.14, -0.99)
# 3. str          → text ("hello", "kris")
# 4. bool         → True / False
# 5. list         → ordered, changeable collection [1, 2, 3]
# 6. tuple        → ordered, NOT changeable (1, 2, 3)
# 7. dict         → key-value pairs {"name": "kris", "age": 20}
# 8. set          → unique items {1, 2, 3}

# ------------------------------------------------------------
# 1. BASIC EXAMPLES OF EACH DATA TYPE
# ------------------------------------------------------------

am_interger = 45                                  # int
a_float = 45.25                                   # float
a_string = "Kris"                                 # str
a_boolean = True                                  # bool
a_list = [2,4,3,3]                                # list
a_tuple = (2,5,2,3)                               # tuple
a_dict = {"name" : "Kris", "age" : "5"}           # dict
a_set = {4,5,3,6}                                 # set

# ------------------------------------------------------------
# 2. TYPE CASTING (Changing one data type to another)
# ------------------------------------------------------------

# Convert str -> int
num_str = "25"
num_int = int(num_str)

# Convert int -> float
num_float = float(num_int)

# Convert str -> int
num_string_again = str(num_int)

print(num_int, num_str, num_float, num_string_again)

# ------------------------------------------------------------
# PRACTICE PROBLEMS (WRITE CODE AFTER THIS COMMENT)
# ------------------------------------------------------------

# Problem 1:
# Create a variable for each data type:
# - Your name (str)
# - Your age (int)
# - Your marks (float)
# - Are you human? (bool)
# - Your favorite numbers (list)
# - A tuple of 3 random values
# - A dictionary storing "name" and "age"
# - A set of 5 unique numbers

your_name = "Kris"
your_age = 41
your_marks = 69.0
are_you_human = False
your_favourite_numbers = [0,5,6]
tuple_of_3_random_values = (5,6,3)
dictionary = {"name" : "Kris", "Age" : 45}
set_of_5_unique = {2,5,6,3,9}

# Problem 2:
# Convert:
# - your age (int) → float
# - your marks (float) → int
# - your name (str) → list of characters
# Example: "kris" → ['k', 'r', 'i', 's']

your_age_float = float(your_age)
your_marks_int = int(your_marks)
your_name_list = list(your_name)

# Problem 3:
# Print:
# - type of every variable you created
# - length of your name
# - max, min of your favorite numbers list

# type of variables
print(type(your_name), type(your_age), type(your_marks), type(are_you_human), type(your_favourite_numbers), type(tuple_of_3_random_values), type(dictionary), type(set_of_5_unique))

# length of name
print(len(your_name))

# Max, min from list
print(max(your_favourite_numbers))
print(min(your_favourite_numbers))

# Problem 4:
# Create a dictionary of:
#   "name", "age", "is_student", "skills"
# where skills is a list like ["python", "dsa"]

dict = {
    "name" : "Kabir",
    "age" : 19,
    "isStudent" : True,
    "skills" : ["python", "dsa", "Flutter"] }

# Then print:
# - all keys
# - all values
# - the value of "skills"

print(dict.keys())          # all keys
print(dict.values())        # all values
print(dict["skills"])       # value of key "skills"

# Problem 5:
# Create variables of all basic datatypes:
# - an integer
# - a float
# - a boolean
# - a string
# Print each variable and also print its datatype using type()

# Write code here

num = 4
percent = 96.30
is_King = True
your_name = "Kris"

print(f"{num} : {type(num)}")
print(f"{percent} : {type(percent)}")
print(f"{is_King} : {type(is_King)}")
print(f"{your_name} : {type(your_name)}")

# Problem 6:
# Create a list named data_list containing:
# - an int, a float, a string, and a boolean
# Print:
# - the full list
# - the datatype of the list
# - datatype of each element inside it

# Write code here

data_list = [1, 12.3, "Kris", True]

print(data_list)
print(type(data_list))
print(type(data_list[0]), type(data_list[1]), type(data_list[2]), type(data_list[3]))

# Problem 7:
# Create a tuple named user_info with:
# - your name
# - your age
# - your city
# Print:
# - the full tuple
# - the datatype of the tuple

# Write code here

user_info = ("Kris", "18", "Ahmedabad")

print(user_info)
print(type(user_info))

# Problem 8:
# Create a dictionary named student_record:
# Keys: "name", "age", "score"
# Values: any name, any age, any score
# Print the dictionary and also print value of "score"

# Write code here

student_record = {"name": "Kris", "age": 19, "score": 96}
print(student_record, student_record["score"])

# Problem 9:
# Create a set named unique_nums containing at least 5 numbers
# (make sure at least one number tries to repeat)
# Print the set and explain in a comment what happened to duplicates.

# Write code here

unique_nums = {1, 2, 3, 4, 1}
print(unique_nums)

# The set in python is designed to take unique values, when we explicitly put non-unique values,
# it will not throw the error but it will remove the duplicates.

# Problem 10:
# Create these variables:
# a_1 = "10"
# b_1 = 20
# Convert a so you can add it with b.
# Print result and datatype before & after conversion.

# Write code here

a_1 = "10"
b_1 = 20

print(type(a_1))
print(type(b_1))

a_1 = int(a_1)
print(type(a_1))

sum_a1_b1 = a_1 + b_1
print(sum_a1_b1)