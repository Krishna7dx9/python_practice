# ============================================================
# PYTHON DECORATORS — EXPLAINED WITH CODE AND REASONS
# ============================================================

import time

# ------------------------------------------------------------
# WHY DECORATORS EXIST
# ------------------------------------------------------------
# We want to ADD extra behavior to a function
# WITHOUT changing the function itself.
#
# Example:
# - logging
# - timing
# - authentication
#
# Decorators solve this cleanly.
# ------------------------------------------------------------

# ------------------------------------------------------------
# STEP 1: FUNCTIONS ARE OBJECTS (WHY THIS MATTERS)
# ------------------------------------------------------------
# Decorators only work because functions are treated like data.

def greet_func():
    print("Hello")

# 'greet' is NOT special syntax
# It is variable holding a function object

another_name = greet_func

# WHY this matters:
# If a function can be assigned,
# it can also be wrapped, replaced, or returned.

# ------------------------------------------------------------
# STEP 2: PASSING A FUNCTION (WHY NEEDED)
# ------------------------------------------------------------
# A decorator must RECEIVE a function to modify it.

def run_func(func):
    # 'func' now refers to greet
    func()

run_func(greet_func)

# WHY:
# The decorator needs access to the function
# so it can control WHEN and HOW it runs.

# ------------------------------------------------------------
# STEP 3: ADDING BEHAVIOR (PROBLEM DEMO)
# ------------------------------------------------------------
# Let’s add behavior before and after greet()

def add_behaviour_func(func):
    print("Before Function")
    func()
    print("After function")

add_behaviour_func(greet_func)

# WHY THIS IS NOT A DECORATOR:
# - It runs immediately
# - We cannot reuse it
# - We cannot call greet normally anymore

# ------------------------------------------------------------
# STEP 4: RETURN A FUNCTION (WRAPPER)
# ------------------------------------------------------------
# Instead of running immediately,
# we RETURN a NEW FUNCTION.

def simple_decorator(func):
    def wrapper_func():
        print("Before function")
        func()
        print("After function")

    # WHY return wrapper:
    # We want delayed execution
    # We want reuse
    return wrapper_func

# ------------------------------------------------------------
# STEP 5: REPLACING THE ORIGINAL FUNCTION
# ------------------------------------------------------------
# This is the CORE IDEA of decorators.

def say_hi_func():
    print("hi") 

# WHAT THIS LINE DOES:
# - decorator receives say_hi
# - decorator returns wrapper
# - say_hi is REPLACED by wrapper
say_hi_func = simple_decorator(say_hi_func)

say_hi_func()

# WHY:
# Now calling say_hi() runs wrapper()
# which internally runs the original function

# ------------------------------------------------------------
# STEP 6: @decorator SYNTAX (WHY IT EXISTS)
# ------------------------------------------------------------
# This is only SYNTAX SUGAR.
# No new behavior.

@simple_decorator
def say_hello_func():
    print("hello")

# Python internally does:
# say_hello = decorator(say_hello)

say_hello_func()

# ------------------------------------------------------------
# STEP 7: WHY *args AND **kwargs ARE REQUIRED
# ------------------------------------------------------------
# Real functions take arguments.
# Decorators must work for ALL functions.

def universal_decorator(func):
    def wrapper(*args, **kwargs):
        # WHY *args, **kwargs:
        # - Accept any number of arguments
        # - Forward them safely
        print("Arguments: ", args, kwargs)
        return func(*args, **kwargs)
    return wrapper

@universal_decorator
def add_func(a, b):
    return a + b

print(add_func(3, 4))

# ------------------------------------------------------------
# STEP 8: METADATA PROBLEM (WHY wraps IS NEEDED)
# ------------------------------------------------------------
# Wrapping hides original function info.

def bad_decorator_func(func):
    def wrapper():
        return func()
    return wrapper

@bad_decorator_func
def demo():
    """important function"""
    pass

# demo.__name__ == 'wrapper'  ❌
# demo.__doc__ == None        ❌

# WHY THIS IS BAD:
# - Debugging becomes hard
# - Logging breaks
# - Frameworks fail

# ------------------------------------------------------------
# STEP 9: FIXING METADATA USING functools.wraps
# ------------------------------------------------------------

from functools import wraps

def good_decorator_func(func):
    @wraps(func)      # WHY
    # Copies name, docstring, annotations

    def wrapper_func(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper_func

@good_decorator_func
def fixed():
    """Metadata preserved"""
    pass

# ------------------------------------------------------------
# STEP 10: DECORATOR WITH PARAMETERS (WHY EXTRA LAYER)
# ------------------------------------------------------------
# Sometimes decorator itself needs configuration.                  

def repeat(times):
    # WHY this layer:
    # To capture decorator arguments

    def decorator_func(func):
        # WHY this layer:
        # To receive the function

        def wrapper_func():
            for _ in range(times):
                func()

        return wrapper_func
    return decorator_func

@repeat(3)
def welcome_func():
    print("Welcome")

# ------------------------------------------------------------
# STEP 11: MULTIPLE DECORATORS (WHY ORDER MATTERS)
# ------------------------------------------------------------

def deco_a(func):
    def wrapper_func():
        print("A before")
        func()
        print("A after")
    return wrapper_func

def deco_b(func):
    def wrapper_func():
        print("B before")
        func()
        print("B after")
    return wrapper_func

@deco_a
@deco_b
def example_func():
    print("Inside")

# Python executes:
# example = deco_a(deco_b(example))

# ============================================================
# DECORATORS TEST 1 — EASY
# ============================================================

# 1. Create a decorator called 'my_decorator' that:
#    - Prints "Before function" before running a function
#    - Prints "After function" after running a function

def my_decorator(func):
    
    def wrapper(*args, **kwargs):
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")
        return result
    return wrapper

@my_decorator
def greet__(name):
    print(f"Good Morning {name}")

greet__("Kris")

# 2. Apply 'my_decorator' to this function using @ syntax:

@my_decorator
def greet_():
    print("Hello World")

# 3. Call greet() AFTER defining it and applying the decorator

greet_()

# 4. Create a decorator called 'args_decorator' that:
#    - Prints "Arguments received:" followed by all args and kwargs
#    - Calls the original function with the same arguments

def args_decorator(func):
    def wrapper(*args, **kwargs):
        print("Arguments received: ", args, kwargs)
        return func(*args, **kwargs)
    return wrapper

@args_decorator
def add_(a, b):
    return a + b

add_(5, 7)

# 5. Apply 'args_decorator' to this function using @ syntax:

@args_decorator
def add(a, b):
    return a + b

# 6. Call add(5, 7) at the end and print the result

print(add(5, 7))

# 7. Create a decorator called 'repeat_decorator' that:
#    - Takes an argument 'times' (integer)
#    - Calls the original function 'times' number of times

def repeat_decorator(times):           
    def decorator(func):
        def wrapper(*args, **kwargs):
            # repeat logic
            for _ in range(times):
                result = func(*args, **kwargs)
            return result 
        return wrapper
    return decorator

@repeat_decorator(3)
def greet():
    print("Hey")

# 8. Apply 'repeat_decorator' to this function using @ syntax:

@repeat_decorator(3)
def say_welcome():
    print("Welcome to Python")

# 9. Create a decorator called 'uppercase_decorator' that:
#    - Converts the string returned by the function to uppercase
#    - Returns the modified string

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)              # calls the original function
        return result.upper()                       # modify the result
    return wrapper

# 10. Apply 'uppercase_decorator' to this function using @ syntax:P

@uppercase_decorator
def greet_user():
    return "hello user"

# 11. Combine decorators: 
#     - Apply 'repeat_decorator(times=2)' and 'uppercase_decorator' to this function
#     - Ensure uppercase happens first, then repeat

@repeat_decorator(2)
@uppercase_decorator
def hello_world():
    return "hello world"

# 12. Create a decorator called 'timer_decorator' that:
#     - Measures execution time of the function in seconds
#     - Prints "Execution time: <time> seconds"
#     - Returns the original function result

import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()                       # before function runs
        result = func(*args, **kwargs)
        end = time.time()                         # after function runs

        print(f"Execution time: {end- start} seconds")
        return result

    return wrapper

# 13. Apply 'timer_decorator' to this function and call it:

@timer_decorator
def compute_sum(n):
    return sum(range(n))

# 14. Create a decorator called `log_decorator` that:
#     - Prints "Function started"
#     - Executes the original function
#     - Prints "Function ended"
#     - Returns the original function’s result

# Apply it using @ syntax on a function `multiply_nums(x, y)`
# that returns x * y.
# Call the function and print the result.

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function Started")
        result = func(*args, **kwargs)
        print("Function Ended")
        return result
    return wrapper

@log_decorator
def multiply_nums(x, y):
    return x * y

print(multiply_nums(5,6))

# 15. Create a decorator called `double_result_decorator` that:
#     - Calls the original function
#     - Doubles the returned value
#     - Returns the doubled value

# Apply it using @ syntax on a function `get_number()`
# that returns an integer of your choice.
# Print the final returned value.


def double_result_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper

@double_result_decorator
def get_number():
    return 5

print(get_number())

# 16. Create a decorator called `check_positive_decorator` that:
#     - Accepts a function with one integer argument
#     - If the argument is negative, print "Negative value not allowed"
#       and return None
#     - Otherwise, call the original function and return its result

# Apply it using @ syntax on a function `square_num(n)`
# that returns n * n.
# Call the function once with a positive number and once with a negative number.

def check_positive_decorator(func):
    def wrapper(n):
        if n < 0:
            print("Negative value not allowed")
            return None
        else:
            result = func(n)
            return result
    return wrapper

@check_positive_decorator
def square_num(n):
    return n * n

# Test with positive number
print(square_num(5))  # Output: 25

# Test with negative number
print(square_num(-3))  # Output: Negative value not allowed, None

# ============================================================
# DECORATORS TEST 2
# ============================================================

# Q1: What is a decorator in Python? (one sentence)

# A decorator is a function that takes another function, extends or modifies its behavior, and returns a new 
# function without changing the original source code.

# Q2: What does the @ symbol do when used above a function?

# @decorator applies the decorator
# It rewrites the function definition as:
# f = decorator(f)

# Q3: Write a decorator named `log_call` that prints "called" before executing a function.
# The decorator must work for any number of arguments.

from functools import wraps

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("called")
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_call
def add(a, b):
    return a + b
    
# Q4: What happens if a decorator’s wrapper does not return the original function’s return value?

# returns None

# Q5: In stacked decorators, which decorator runs first at runtime — top or bottom?

# bottom

# Q6: Why is functools.wraps important? Name two things it preserves.

# To prevent loss of meta data of original function. __name__, __doc__

# Q7: Write a decorator `times(n)` that executes a function `n` times.
# Use correct decorator-with-arguments structure.

def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def add(a, b):
    return a + b            

# Q8: Given:
# @d1
# @d2
# def f():
#     pass
# Rewrite this WITHOUT using @ syntax.

# f = d1(d2(f))

# Q9: True or False:
# A decorator can modify a function without changing its source code.

# True

# Q10: Identify the bug (do not fix it):

# def dec(func):
#     def wrapper():
#         func()
#     return wrapper
#
# @dec
# def add(a, b):
#     return a + b

# wrapper function does'nt handling arguments