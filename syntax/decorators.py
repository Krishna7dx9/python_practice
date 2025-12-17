# ============================================================
# PYTHON DECORATORS — EXPLAINED WITH CODE AND REASONS
# ============================================================

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

def greet():
    print("Hello")

# 'greet' is NOT special syntax
# It is variable holding a function object

another_name = greet

# WHY this matters:
# If a function can be assigned,
# it can also be wrapped, replaced, or returned.

# ------------------------------------------------------------
# STEP 2: PASSING A FUNCTION (WHY NEEDED)
# ------------------------------------------------------------
# A decorator must RECEIVE a function to modify it.

def run(func):
    # 'func' now refers to greet
    func()

run(greet)

# WHY:
# The decorator needs access to the function
# so it can control WHEN and HOW it runs.

# ------------------------------------------------------------
# STEP 3: ADDING BEHAVIOR (PROBLEM DEMO)
# ------------------------------------------------------------
# Let’s add behavior before and after greet()

def add_behaviour(func):
    print("Before Function")
    func()
    print("After function")

add_behaviour(greet)

# WHY THIS IS NOT A DECORATOR:
# - It runs immediately
# - We cannot reuse it
# - We cannot call greet normally anymore

# ------------------------------------------------------------
# STEP 4: RETURN A FUNCTION (WRAPPER)
# ------------------------------------------------------------
# Instead of running immediately,
# we RETURN a NEW FUNCTION.

def decorator(func):

    def wrapper():
        print("Before function")
        func()
        print("After function")

    # WHY return wrapper:
    # We want delayed execution
    # We want reuse
    return wrapper

# ------------------------------------------------------------
# STEP 5: REPLACING THE ORIGINAL FUNCTION
# ------------------------------------------------------------
# This is the CORE IDEA of decorators.

def say_hi():
    print("hi") 

# WHAT THIS LINE DOES:
# - decorator receives say_hi
# - decorator returns wrapper
# - say_hi is REPLACED by wrapper
say_hi = decorator(say_hi)

say_hi()

# WHY:
# Now calling say_hi() runs wrapper()
# which internally runs the original function

# ------------------------------------------------------------
# STEP 6: @decorator SYNTAX (WHY IT EXISTS)
# ------------------------------------------------------------
# This is only SYNTAX SUGAR.
# No new behavior.

@decorator
def say_hello():
    print("hello")

# Python internally does:
# say_hello = decorator(say_hello)

say_hello()

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
        return func(*args, **kwargs)
    
    return wrapper

@universal_decorator
def add(a, b):
    return a + b

print(add(3, 4))

# ------------------------------------------------------------
# STEP 8: METADATA PROBLEM (WHY wraps IS NEEDED)
# ------------------------------------------------------------
# Wrapping hides original function info.

























