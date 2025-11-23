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
while value !=10:
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