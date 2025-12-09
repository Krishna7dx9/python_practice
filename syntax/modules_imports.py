# ------------------------------------------------------------
# Modules & Imports in Python
# ------------------------------------------------------------

# 1. Importing a built-in module

import math
print(math.sqrt(25))                  # 5.0

# 2. Using alias
import math as m
print(m.factorial(5))                 # 120

# 3. Importing specific names
from math import pi, sin
print(pi)                             # 3.14
print(sin(0))                         # 0.0

# 4. Importing your own module

# Suppose helper.py contains:
# def greet(name):
#     return f"Hello {name}"

import helper
print(helper.greet("Kris"))

from helper import greet
print(greet("Kris Again"))
