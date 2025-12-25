# ------------------------------------------------------------
# Modules & Imports in Python
# ------------------------------------------------------------

# 1. Importing a built-in module

import math
print(math.sqrt(25))                    # 5

# 2. Using alias
import math as m
print(m.factorial(5))                  # 120

# 3. Importing specific names
from math import pi, sin
print(pi)                              # 3.141592653589793
print(sin(0))                          # 0.0

# 4. Importing your own module

# Suppose helper.py contains:
# def greet(name):
#     return f"Hello {name}"

# import helper
# print(helper.greet("Kris"))

# from helper import greet
# print(greet("Kris Again"))

# 5. __name__ and __main__

def add(a, b):
    return a + b

if __name__ == "__main__":
    print("Running directly: ", add(2, 3))

# ------------------------------------------------------------
# TEST: Modules & Imports
# Complete every task without help.
# ------------------------------------------------------------

# Q1. Import the built-in math module and:
#     (a) Print the square root of 144
#     (b) Print the value of pi

import math
print("Square Root of 144 is: ", math.sqrt(144))
print("The value of pi is: ", math.pi)

# Q2. Import the random module using an alias "r"
#     Then print a random integer between 1 and 50.

import random as r
print("Random Integer between 1 and 50: ", r.randint(1, 50))

# Q3. From the math module, import only factorial
#     Then print factorial of 6.

from math import factorial
print("Factorial of 6 is: ", factorial(6))

# Q4. Import ONLY the choice and shuffle functions from random.
#     Then:
#         (a) Use choice to pick a random element from [1, 2, 3, 4, 5]
#         (b) Shuffle a list [10, 20, 30, 40] and print it

from random import choice, shuffle

print("Random element from [1, 2, 3, 4, 5]: ", choice([1, 2, 3, 4, 5]))
lst = [10, 20, 30, 40]
shuffle(lst)
print("Shuffled a list [10, 20, 30, 40]: ", lst)

# Q5. Import the statistics module as "stats".
#     Then print:
#         stats.mean([5, 10, 15])
#         stats.median([1, 2, 3, 4])

import statistics as stats
print("Statistics mean: ", stats.mean([5, 10, 15]))
print("Statistics median: ", stats.median([1, 2, 3, 4]))

# Q6. Demonstrate "import as" for two different modules:
#         import math as m
#         import random as r
#     Then print:
#         m.factorial(6)
#         r.random()

import math as m
import random as r

print("Factorial of 6: ", m.factorial(6))
print("Random: ", r.random())

# Q7. Demonstrate what happens with __name__.
#     Write:
#         print(__name__)
#
#     (Do not write if-conditions here; just print it.)

print(__name__)

# As this file is executes directly this file variable got assigned __main__