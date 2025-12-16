# ============================================================
# PYTHON DECORATORS 
# ============================================================

# ------------------------------------------------------------
# 1.  A FUNCTION IS JUST A VARIABLE
# ------------------------------------------------------------

def greet():
    print("Hello")

# 'greet' is just a variable pointing to a function
another_name = greet

# another_name() does the same thing as greet()

# ------------------------------------------------------------
# 2. FUNCTION PASSED AS ARGUMENT / A FUNCTION CAN BE PASSED INTO ANOTHER FUNCTION
# ------------------------------------------------------------

def call_function(func):
    # 'func' is a function object
    func()

# call_function(greet) would execute greet()
call_function(greet)                                     

# ------------------------------------------------------------
# 3. ADD EXTRA BEHAVIOR AROUND A FUNCTION
# ------------------------------------------------------------

def add_behavior(func):
    print("Before function")
    func()
    print("After Function")

add_behavior(greet)

# ------------------------------------------------------------
# 4. RETURN A NEW FUNCTION (WRAPPER)
# ------------------------------------------------------------

def decorator(func):

    def wrapper():
        print("Before function")
        func()
        print("After function")

    # IMPORTANT:
    # we return the wrapper function
    return wrapper

# ------------------------------------------------------------
# 5. MANUALLY APPLY THE DECORATOR
# ------------------------------------------------------------

def say_hi():
    print("Hi")

# This line is the core idea of decorators  
say_hi = decorator(say_hi)

say_hi()

# Original say_hi is now wrapped

# ------------------------------------------------------------
# 6. USING @ SYNTAX (NO NEW LOGIC)
# ------------------------------------------------------------

@decorator 
def say_hello():
    print("Hello")

# Python internally does
# say_hello = decorator(say_hello)

say_hello()

# ------------------------------------------------------------
# STEP 7: DECORATORS WITH ARGUMENTS (*args, **kwargs)
# ------------------------------------------------------------

def decorator_with_args(func):

    def wrapper(*args, **kwargs):
        print("Arguments: ", args, kwargs)
        return func(*args, **kwargs)
    
    return wrapper

@decorator_with_args
def add(a, b):
    print(a + b)

add(3, 4)







