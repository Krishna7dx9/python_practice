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
a_floar = 45.25                                   # float
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
your_marks = 69
are_you_human = False
your_favourite_numbers = []
tuple_of_3_random_values = (5,6,3)
dictionary = {"name" : "Kris", "Age" : 45}
set_of_5_unique = {2,5,6,3,9}


# Problem 2:
# Convert:
# - your age (int) → float
# - your marks (float) → int
# - your name (str) → list of characters
# Example: "kris" → ['k', 'r', 'i', 's']


# Problem 3:
# Print:
# - type of every variable you created
# - length of your name
# - max, min of your favorite numbers list


# Problem 4:
# Create a dictionary of:
#   "name", "age", "is_student", "skills"
# where skills is a list like ["python", "dsa"]

# Then print:
# - all keys
# - all values
# - the value of "skills"