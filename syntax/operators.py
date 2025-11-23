# Python Operators — Full Syntax Guide
# This file teaches every operator you MUST know before touching DSA.
# Read → Understand → Write your own mini examples.
# Never skip.

# 1. Arithmetic Operators
# ------------------------
# +, -, *, /, //, %, **

a = 10
b = 3

add = a + b
sub = a - b
mul = a * b
div = a / b
floor = a // b
mod = a % b
power = a ** b

# 2. Assignment Operators
# ------------------------

x = 5
x += 2
x -= 1
x *= 3
x /= 2
x //= 2
x **= 2
x %= 5

# 3. Comparison Operators
# -----------------------
# ==, !=, >, <, >=, <=

p = 10
q = 20

is_equal = p == q
not_equal = p != q
gt = p > q
lt = p < q
ge = p >= q
le = p <= q

# 4. Logical Operators
# ---------------------
# and, or, not

x = True
y = False

logical_and = x and y
logical_or = x or y
logical_not = not x

# 5. Identity Operators
# ----------------------
# is, is not

list1 = [1,2,3]
list2 = [1,2,3]
list3 = list1

same_obj = list1 is list3
not_same_obj = list1 is not list3

# 6. Membership Operators
# ------------------------
# in, not in

nums = [10, 20, 30, 40]

check_in = 20 in nums
does_not_exist = 100 not in nums

# 7. Bitwise Operators
# ---------------------
# &, |, ^, ~, <<, >>

m = 5
n = 3

bit_and = m & n
bit_or = m | n
bit_xor = m ^ n
bit_not = ~m            # -(m + 1)
shift_left = m << 1
shift_right = m >> 1


# 🔹 Problem 1 — Arithmetic Operators
#
# Create two integers:
# i = 17
# v = 4
#
# Calculate and print:
# Sum
# Difference
# Product
# Quotient (/)
# Floor division (//)
# Modulus (%)
# a raised to b (**)

i = 17
v = 4

result_sum = i + v
print(result_sum)

difference = i - v
print(difference)

product = i * v
print(product)

quotient = i / v
print(quotient)

floor_division = i // v
print(floor_division)

modulus = i % v
print(modulus)

power = i ** v
print(power)


# 🔹 Problem 2 — Comparison Operators

# Create:
# l = 55
# k = 32

# Print the result (True/False) for:

# l > k
# l < k
# l == k
# l != k
# l >= k
# l <= k

l = 55
k = 32

print(l > k)
print(l < k)
print(l == k)
print(l != k)
print(l >= k)
print(l <= k)

# 🔹 Problem 3 — Logical Operators

# Define:
 
# logged_in = True
# is_admin = False

# Print:
# logged_in AND is_admin
# logged_in OR is_admin
# NOT is_admin

logged_in = True
is_admin = False

print(logged_in and is_admin)
print(logged_in or is_admin)
print(not is_admin)

# 🔹 Problem 4 — Assignment Operators

# Start with:
# score = 50
# Update score using:
# Add 10
# Subtract 5
# Multiply by 2
# Divide by 5
# Floor divide by 2
# Modulus by 3
# Raise to power 2
# After every step, print the updated score.

score = 50
print(score)
score += 10
print(score)
score -= 5
print(score)
score *= 2
print(score)
score /= 5
print(score)
score //= 2
print(score)
score %= 3
print(score)
score **= 2
print(score) 

# 🔹 Problem 5 — Identity & Membership

# Create:

# numbers = [10, 20, 30, 40]
# letters = "python"

# Print:

# Check if 20 is in numbers
# Check if 25 is not in numbers
# Check if "t" is in letters
# Check if "z" not in letters
# Check if numbers is numbers (identity)
# Check if numbers is a copy of numbers → numbers_copy = nums[:]

numbers = [10,20,30,40]
letters = "python"

print(20 in numbers)
print(25 not in numbers)
print("t" in letters)
print("z" not in letters)
print(numbers is numbers)
numbers_copy = numbers[:]
print(numbers is numbers_copy)