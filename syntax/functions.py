# ============================================================
# FUNCTIONS IN PYTHON — COMPLETE SYNTAX
# ============================================================

# ------------------------------------------------------------
# 1. Basic function definition
# ------------------------------------------------------------
# A function is created using `def`
# It only runs when you CALL it.

def greet():
    print("Hello from a function!")

# ------------------------------------------------------------
# 2. Function with parameters
# ------------------------------------------------------------
# Parameters = values you PASS into a function

def greet_person(name):
    print(f"Hello, {name}!")

# ------------------------------------------------------------
# 3. Function with TWO parameters
# ------------------------------------------------------------

def add_number(a, b):
    return a + b             # return sends value OUT of function

# ------------------------------------------------------------
# 4. Function with a DEFAULT parameter
# ------------------------------------------------------------
# If no value is passed → default value is used

def welcome(user="Guest"):
    print(f"Welcome, {user}!")

# ------------------------------------------------------------
# 5. Function returning MULTIPLE values
# ------------------------------------------------------------
# Python returns multiple values as a tuple

def math_operations(x, y):
    add = x + y
    sub = x - y
    mul = x * y
    return add, sub, mul

# ------------------------------------------------------------
# 6. Keyword arguments
# ------------------------------------------------------------
# You can pass arguments by name

def user_info(name, age):
    print(f"Name: {name}, Age: {age}")

# user_info(age=30, name="Kris")
# Order doesn’t matter when key=value is used

# ------------------------------------------------------------
# 7. Arbitrary arguments (*args → multiple values)
# ------------------------------------------------------------
# When you don’t know how many arguments the user will pass

def sum_all(*nums):
    total = 0
    for n in nums:
        total += n
    return total

# ------------------------------------------------------------
# 8. Arbitrary keyword arguments (**kwargs)
# ------------------------------------------------------------
# Accepts unlimited key=value pairs

def print_details(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

# ------------------------------------------------------------
# 9. Function inside a function (Nested functions)
# ------------------------------------------------------------

def outer():
    def inner():
        return  "Inside inner functions"
    return inner()

# ------------------------------------------------------------
# 10. Lambda functions (one-line SMALL functions)
# ------------------------------------------------------------

square = lambda x: x * x
add_lambda = lambda a, b: a + b


# ------------------------------------------------------------
# Problem 1:
# Create a function called say_hello that:
# - takes a name
# - prints "Hello, <name>!"
# ------------------------------------------------------------

def say_hello(name):
    print(f"Hello, {name}!")

# ------------------------------------------------------------
# Problem 2:
# Create a function multiply_three that:
# - takes 3 numbers
# - returns their product
# ------------------------------------------------------------

def multiply_three(g, h, j):
    product =  g * h * j
    return product

# ------------------------------------------------------------
# Problem 3:
# Create a function describe_person with:
# - 2 parameters: person_name, city
# - prints: "<person_name> lives in <city>"
# ------------------------------------------------------------

def describe_person(person_name, city):
    print(f"{person_name} lives in {city}")

# ------------------------------------------------------------
# Problem 4:
# Create a function called find_stats that:
# - takes a list of numbers
# - returns (max, min, sum)
# ------------------------------------------------------------

def find_stats(numbers):
    return max(numbers), min(numbers), sum(numbers)

# ------------------------------------------------------------
# Problem 5:
# Create a function bonus_points with DEFAULT parameter:
# - takes score and bonus=10
# - returns score + bonus
# ------------------------------------------------------------

def bonus_points(score, bonus = 10):
    return score + bonus

# ------------------------------------------------------------
# Problem 6:
# Create sum_any function using *args that:
# - accepts ANY number of integers
# - returns the total
# ------------------------------------------------------------

def sum_any(*nums):
    total = 0
    for n in nums:
       total += n
    return total

# ------------------------------------------------------------
# Problem 7:
# Create a function show_profile using **kwargs
# - print all key:value pairs
# Example:
#     show_profile(name="Kris", age=21, skill="Python")
# ------------------------------------------------------------

def show_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

# ------------------------------------------------------------
# Problem 8:
# Write a lambda function:
# - input: a number
# - output: number squared
# Store it in: square_num
# ------------------------------------------------------------

square_num = lambda num_a: num_a * num_a