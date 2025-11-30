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

# ------------------------------------------------------------
# Problem 9:
# Create a function called greet_users that:
# - takes a list of names
# - prints "Hello, <name>!" for each name
# Example: greet_users(["Kris","Alex"]) → prints:
# Hello, Kris!
# Hello, Alex!
# ------------------------------------------------------------

# Write your code below
def greet_users(names):
        for name in names:
            print(f"Hello, {name}!")


# ------------------------------------------------------------
# Problem 10:
# Create a function calculate_power that:
# - takes 2 numbers: base and exponent
# - returns base ** exponent
# ------------------------------------------------------------

# Write your code below

def calculate_power(base, exponent):
    return base ** exponent

# ------------------------------------------------------------
# Problem 11:
# Create a function filter_even that:
# - takes a list of integers
# - returns a new list containing only even numbers
# ------------------------------------------------------------

# Write your code below

def filter_even(integers):
    new_list = []
    for n in integers:
        if n % 2 == 0:
            new_list.append(n)
    return new_list

# ------------------------------------------------------------
# Problem 12:
# Create a function factorial using recursion:
# - input: n
# - output: factorial of n
# ------------------------------------------------------------

# Write your code below

def factorial(n): 
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)

# ------------------------------------------------------------
# Problem 13:
# Create a function swap_numbers that:
# - takes two numbers a and b
# - returns them swapped
# ------------------------------------------------------------

# Write your code below

def swap_numbers(a, b):
    return (b , a)

# ------------------------------------------------------------
# Problem 14:
# Write a lambda function triple that:
# - input: a number
# - output: number * 3
# ------------------------------------------------------------

# Write your code below

triple = lambda number: number * 3

# 15. Write a function `square(n)` that returns the square of a number.

def square(n):
    return n ** 2

# 16. Write a function `is_even(n)` that returns True if n is even, else False.

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# 17. Write a function `max_of_two(a, b)` that returns the larger number.

def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b

# 18. Write a function `reverse_string(s)` without using slicing.

def reverse_string(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev

# 19. Write a recursive function `sum_upto(n)` that returns 1 + 2 + ... + n.

def sum_upto(n):
     if n == 0:
         return n
     else:
         return n + sum_upto(n - 1)

# 20. Write a recursive function `power(base, exp)` that calculates base^exp.

def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)

# 21. Write a function that swaps three numbers (a → b → c → a).

def swap(a, b, c):
    return b, c, a

# 22. Write a lambda function `last_digit` that returns the last digit of a number.



# 23. Write a function `count_vowels(s)` that returns the number of vowels in a string.

# 24. Write a function `merge_lists(l1, l2)` that returns a single combined list.

# 25. Write a function `is_palindrome(s)` that checks if a string is palindrome.

# 26. Write a function `min_of_three(a, b, c)` without using min().

# 27. Write a function `factorial_iterative(n)` using loop (not recursion).

# 28. Write a function `unique_elements(lst)` that returns list of unique elements.

# 29. Write a function `multiply_list(lst)` that multiplies all numbers in a list.

# 30. Write a function `safe_divide(a, b)` that returns "Error" if b == 0 else a/b.
