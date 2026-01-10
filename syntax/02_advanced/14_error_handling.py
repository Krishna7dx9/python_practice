# ============================================================
# ERROR HANDLING — COMPLETE SYNTAX
# ============================================================

# 1. Basic try-except

try:
    x = int(input("Enter an integer: "))
except ValueError:
    print("Error: That was not a valid integer!")

print()

# 2. Catching multiple exceptions separately

try:
    num = int(input("Enter a number to divide 10 by: "))
    result = 10 / num
except ValueError:
    print("Error: Invalid Number!")
except ZeroDivisionError:
    print("Error cannot divide by zero!")

print()

# 3. Catching multiple exceptions at once

try:
    val = int(input("Enter a number to divide 20 by: "))
    outcome = 20 / val
except (ValueError, ZeroDivisionError) as e:
    print("Error occurred: ", e)

print()

# 4. try-except-else

try:
    num2 = int(input("Enter a number to divide 30 by: "))
    res = 30 / num2
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Error Invalid number!")
else:
    print("Division successful! Result: ", res)

print()

# 5. try-except-finally

try:
    file = open("test.txt", "r")
except FileNotFoundError:
    print("File not found!")
finally:
    print("Finally executed. This always runs.")

print()

# 6. Optional: showing exception object

try:
    num3 = int(input("Enter a number: "))
    result2 = 100 / num3
except Exception as err:
    print("Caught as exception: ", err)

print("End of error handling examples")

# ------------------------------------------------------------
# PYTHON ERROR HANDLING TEST
# Fill code for each question
# ------------------------------------------------------------

# Q1. Write a try-except block to catch a ValueError
#     Convert input string to integer

try:
    a = int(input("Enter a number: "))
except ValueError:
    print("Error! Invalid Number")

# Q2. Write a try-except block to catch ZeroDivisionError
#     Divide 10 by a user input number

try:
    b = int(input("Enter a number: "))
    result_b = 10 / b
except ZeroDivisionError:
    print("This cannot divide by zero")

# Q3. Catch multiple exceptions at once: ValueError or ZeroDivisionError
#     Ask for user input, divide 10 by it, print appropriate message

try:
    c = int(input("Enter a number: "))
    result_c = c / 10
except (ValueError, ZeroDivisionError) as e:
    print("Error occuered", e)

# Q4. Use try-except-else
#     Try dividing 20 by user input
#     If no exception, print "Division successful: <result>"

try:
    d = int(input("Enter a number: "))
    result_d = 20 / d
except ValueError:
    print("Error! This is not correct input")
except ZeroDivisionError:
    print("Error! Can't be divide by zero")
else:
    print("Division successful: ", result_d)

# Q5. Use try-except-finally
#     Try opening a file named "test.txt"
#     If FileNotFoundError, print "File not found"
#     Finally, print "Execution completed"

try:
    file = open("test.txt")
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution completed")

# ============================================================
# ERROR HANDLING — TEST 2
# ============================================================

# Q1
# What is the difference between an error and an exception in Python?
# (one sentence)

# An exception is a runtime error that Python detects and can handle,
# whereas an error is the broader concept of a problem that disrupts program execution.

# Q2
# What will be printed?
try:
    x = 5 / 0
except ZeroDivisionError:
    print("A")
print("B")

# A
# B

# Q3
# Which block runs if NO exception occurs?
# (write the block name only)

# else

# Q4
# What will be printed?
try:
    x = int("10")
except ValueError:
    print("X")
else:
    print("Y")
finally:
    print("Z")

# Y
# Z

# Q5
# Fill in the blank to catch BOTH ValueError and TypeError
try:
    x = int(None)
except __________:
    print("Error caught")

# (ValueError, TypeError)

# Q6
# True or False:
# The finally block runs only if an exception occurs.

# False

# Q7
# What object does `e` represent here?
try:
    1 / 0
except ZeroDivisionError as e:
    pass

# e is the exception object instance, containing:
# the error message
# the exception type instance

# ============================================================
# GENERIC EXCEPT — TEST 3
# ============================================================

# Q1
# True or False:
# A bare `except:` also catches KeyboardInterrupt.

# True


# Q2
# Which is safer?
# (write exactly one)
# a) except:
# b) except Exception:

# except Exception:


# Q3
# Where is generic except allowed?
# (one phrase)

# At top-level / application boundaries


# Q4
# What is the biggest danger of using generic except in core logic?
# (one short phrase)

# Hides bugs


# Q5
# Fill the blank with the BEST practice:
try:
    risky()
except Exception:
    handle_error()

# ============================================================
# ERROR HANDLING — TEST 4 (RAISE)
# ============================================================

# Q1
# What does `raise` do in Python?
# (one sentence)

# It manually triggers an exception and stops normal execution.


# Q2
# What will happen?
def f():
    raise ValueError("X")

f()
print("DONE")

# ValueError is raised
# "DONE" is NOT printed


# Q3
# Fill the blank to re-raise the same exception
try:
    int("abc")
except ValueError:
    raise


# Q4
# True or False:
# You can raise a string as an exception.

# False


# Q5
# Write a single line to raise a TypeError with message "Wrong type"

raise TypeError("Wrong type")


# Q6
# What must a custom exception inherit from?
# (write the class name only)

# Exception
