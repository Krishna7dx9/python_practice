# ============================================================
#                         LOOPS IN PYTHON
# ============================================================

# ------------------------------------------------------------
# 1. FOR LOOP (used when you know HOW MANY times to repeat)
# ------------------------------------------------------------

# Basics for loops 

for i in range(5):
    print(i)

# range(a, b) → starts at a, ends at b-1

for x in range(5, 7):
    print(x)

# range with step    

for j in range(2, 10, 2):
    print(j)

# Loop through a list

nums = [10, 20, 30]
for n in nums:
    print(n)

# Loop through a string

word = "Kris"
for char in word:
    print(char)

# ------------------------------------------------------------
# 2. WHILE LOOP (used when you DON'T know how many times)
# ------------------------------------------------------------

# Basic while loop
count = 1
while count <= 5:
    print(count)
    count += 1

# While loop example: stop when value becomes 10

value = 1
while value != 10:
    print(value)
    value += 1

# ------------------------------------------------------------
# 3. LOOP CONTROL: break, continue, pass
# ------------------------------------------------------------

# break → stop the loop completely
for k in range(18):
    if k == 4:
        break
    print(k)

# continue → skip the current iteration
for m in range(6):
    if m == 2:
        continue
    print(m)

# pass → placeholder (does nothing)
for t in range(3):
    pass                                       # useful when writing empty blocks

# ------------------------------------------------------------
# 4. Nested loops
# ------------------------------------------------------------

for a in range(2):
    for b in range(3):
        print(a, b)

# Exercise 1 — Square of Numbers
# Print:
# 12345
# 12345
# 12345
# 12345
# 12345
#
# Write your code below
# ------------------------------------------------------------

for i in range(1, 6):
    for l in range(1, 6):
        print(l, end = "")
    print()

# ------------------------------------------------------------
# Exercise 2 — Right Triangle of Numbers
# Print:
# 1
# 12
# 123
# 1234
# 12345
#
# Write your code below
# ------------------------------------------------------------

for i in range(5):
    for l in range(i + 1):
        print(l + 1, end = "")
    print()

# ------------------------------------------------------------
# Exercise 3 — Reverse Triangle of Stars
# Print:
# *****
# ****
# ***
# **
# *
#
# Write your code below
# ------------------------------------------------------------

for i in range(5):
    for l in range(5 - i):
        print("*", end = "")
    print()

# ============================================================
# PRACTICE PROBLEMS — LOOPS
# ============================================================

# ------------------------------------------------------------
# Problem 1:
# Print numbers from 1 to 20 using a for loop.
# ------------------------------------------------------------

for z in range(1, 21):
    print(z)

# ------------------------------------------------------------
# Problem 2:
# Using a while loop, print only even numbers from 2 to 20.
# (Use a new variable, e.g., counter_even)
# ------------------------------------------------------------

counter_even = 2
while counter_even <= 20:
    print(counter_even)
    counter_even += 2

# ------------------------------------------------------------
# Problem 3:
# Loop through the string "developer" and print characters 
# except 'e' using continue. Use variable: ch
# ------------------------------------------------------------

for ch in "developer":
    if ch == "e":
        continue
    print(ch)

# ------------------------------------------------------------
# Problem 4:
# Create a list [3, 7, 12, 5, 9]
# Print all numbers until you find 12, then STOP using break.
# Use variable: item
# ------------------------------------------------------------

numbers = [3, 7, 12, 5, 9]
for item in numbers:
    if item == 12:
        break
    print(item)

# ------------------------------------------------------------
# Problem 5:
# Nested Loop:
# Print a rectangle of stars of 3 rows and 5 columns.
# Example:
# *****
# *****
# *****
# ------------------------------------------------------------

for row in range(3):
    for col in range(5):
        print("*", end = "")
    print()                           # <-- moves to next line

# ------------------------------------------------------------
# Problem 6:
# Sum all numbers from 1 to 50 using a loop (you choose for/while).
# Store answer in sum_result and print it.
# ------------------------------------------------------------

sum_result = 0
h = 1
while h <= 50:
    sum_result += h
    h += 1

print(sum_result)

# 🔹 Problem 7 — Multiples Sum
# Calculate and print the sum of all multiples of 3 between 1 and 100.
# Use a loop and store result in sum_multiples

sum_multiples = 0

# Write your code below

sum_multiples = 0
for i in range(1, 100):
    if i % 3 == 0:
        sum_multiples += i
print(f"Sum of multiples of 3 between 1 and 100: {sum_multiples}")

# 🔹 Problem 8 — Character Counter
# Given string text = "programming", count and print how many times 'g' appears.
# Use a loop and a counter variable: g_count

text = "programming"
g_count = 0

# Write your code below

for x in text:
    if "g" == x:
        g_count += 1
print(f"Count: {g_count}")    

# 🔹 Problem 9 — First Negative Finder
# Given list nums = [4, -3, 7, -1, 2, -8], 
# print the first negative number and stop the loop using break

nums = [4, -3, 7, -1, 2, -8]

# Write your code below

for x in nums:
    if x < 0:
        print(x)
        break

# 🔹 Problem 10 — Pattern Printing
# Print a right-angled triangle of stars with 5 rows.
# Example:
# *
# **
# ***
# ****
# *****
# Use nested loops

# Write your code below

for row in range(6):
    for col in range(row):
        print("*", end = "")
    print()

# 🔹 Problem 11 — Square Pattern
# Print a 5x5 square of stars.
# *****
# *****
# *****
# *****
# *****

# Write your code below

for row in range(5):
    for col in range(5):
        print("*", end = "")
    print()

# 🔹 Problem 12 — Increasing Number Triangle
# 1
# 12
# 123
# 1234
# 12345

# Write your code below

for row in range(6):
    for col in range(1, row + 1):
        print(col, end = "")
    print()

# 🔹 Problem 13 — Decreasing Star Triangle
# *****
# ****
# ***
# **
# *

# Write your code below

for row in range(5, 0, -1):
    for col in range(row):
        print("*", end = "")
    print()

# 🔹 Problem 14 — Left-Aligned Pyramid
#     *
#    **
#   ***
#  ****
# *****

# Write your code below

for row in range(5):
    for col in range(row):
        print("*", end ="")
    print()

# 🔹 Problem 15 — Right-Aligned Pyramid
# *
# **
# ***
# ****
# *****

# Write your code below




# 🔹 Problem 16 — Centered Pyramid
#     *
#    ***
#   *****
#  *******
# *********

# Write your code below




# 🔹 Problem 17 — Inverted Centered Pyramid
# *********
#  *******
#   *****
#    ***
#     *

# Write your code below




# 🔹 Problem 18 — Hollow Square
# *****
# *   *
# *   *
# *   *
# *****

# Write your code below




# 🔹 Problem 19 — Hollow Triangle
# *
# **
# * *
# *  *
# *****

# Write your code below




# 🔹 Problem 20 — Number Pyramid
#     1
#    222
#   33333
#  4444444
# 555555555

# Write your code below