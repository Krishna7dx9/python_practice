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

# 🔹 Problem 6 — Conditional Operator Logic
# Given a number n, print "EVEN" if n is even, "ODD" if n is odd
# You MUST use %, comparison and logical operators

n = 15  # change the value to test

# Write your code below

if n % 2 == 0:
    print("EVEN")
elif n % 2 != 0:
    print("ODD")

# 🔹 Problem 7 — Range Classifier Using Operators
# Given a score, classify as:
# "LOW" if score < 40
# "MEDIUM" if 40 <= score <= 70
# "HIGH" if score > 70
# You MUST use logical and comparison operators

score = 55  # change the value to test

# Write your code below

if score < 40:
    print("LOW")
elif 40 <= score <= 70:
    print("MEDIUM")
else:
    print("HIGH")

# 🔹 Problem 8 — Password Strength Checker
# Given a password string:
# Print "STRONG" if length >= 8 AND contains '@' or '#'
# Print "WEAK" otherwise
# You MUST use membership, logical and comparison operators

password = "hello@123"  # change the password to test

# Write your code below

password_length = len(password)

if password_length >= 8 and ("@" in password or "#" in password):
    print("STRONG")
else:
    print("WEAK")

# 🔹 Problem 9 — Bitwise Challenge
# Given two integers a and b, print:
# a & b, a | b, a ^ b, a << 1, b >> 2

a = 12
b = 5

# Write your code below

_1 = a & b
_2 = a | b
_3 = a ^ b
_4 = a << 1
_5 = b >> 2

print(_1)
print(_2)
print(_3)
print(_4)
print(_5)

# 🔹 Problem 10 — Multi-Condition Evaluator
# Given integer x:
# Print "NEGATIVE" if x < 0
# Print "ZERO" if x == 0
# Print "POSITIVE SMALL" if 0 < x <= 10
# Print "POSITIVE LARGE" if x > 10
# Use chained conditions, comparison and logical operators

x = -3  # change the value to test

# Write your code below

if x < 0:
    print("NEGATIVE")
elif x == 0:
    print("ZERO")
elif 0 < x <= 10:
    print("POSITIVE SMALL")
elif x > 10:
    print("POSITIVE LARGE")

# 🔹 Problem 11 — Divisibility Checker
# Given a number num, print:
# "Divisible by 3 and 5" if divisible by both
# "Divisible by 3 only" if divisible by 3 but not 5
# "Divisible by 5 only" if divisible by 5 but not 3
# "Not divisible by 3 or 5" otherwise
# Use %, comparison and logical operators

num = 30  # change to test

# Write your code below

if num % 3 == 0 and num % 5 == 0:
    print("Divisible by 3 and 5")
elif num % 3 == 0 and num % 5 != 0:
    print("Divisible by 3 only")
elif num % 5 == 0 and num % 3 != 0:
    print("Divisible by 5 only")
else:
    print("Not divisible by 3 or 5")

# 🔹 Problem 12 — Leap Year Detector
# Given year, print "LEAP YEAR" if it is a leap year
# Rules:
# - divisible by 4 AND not divisible by 100 OR divisible by 400
# Use %, comparison and logical operators

year = 2000  # change to test

# Write your code below

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("LEAP YEAR")

# 🔹 Problem 13 — Number Sign & Parity
# Given an integer n, print:
# "POSITIVE EVEN", "POSITIVE ODD", "NEGATIVE EVEN", "NEGATIVE ODD", or "ZERO"
# Use %, comparison and logical operators

n = -8  # change to test

# Write your code below

if n > 0 and n % 2 == 0:
    print("POSITIVE EVEN")
elif n > 0 and n % 2 != 0:
    print("POSITIVE ODD")
elif n < 0 and n % 2 == 0:
    print("NEGATIVE EVEN")
elif n < 0 and n % 2 != 0:
    print("NEGATIVE ODD")
else:
    print("ZERO")

# 🔹 Problem 14 — Range & Divisibility
# Given an integer n (1–100):
# Print:
# - "LOW MULTIPLE OF 3" if n <= 50 and divisible by 3
# - "HIGH MULTIPLE OF 5" if n > 50 and divisible by 5
# - "OTHER" otherwise
# Use %, comparison and logical operators

n = 45  # change to test

# Write your code below

if n <= 50 and n % 3 == 0:
    print("LOW MULTIPLE OF 3")
elif n > 50 and n % 5 == 0:
    print("HIGH MULTIPLE OF 5")
else:
    print("OTHER")

# 🔹 Problem 15 — Bitwise & Parity Combo
# Given two integers a and b:
# Print:
# - "BOTH EVEN" if both even
# - "BOTH ODD" if both odd
# - "ONE EVEN ONE ODD" otherwise
# Also print a ^ b
# Use %, bitwise, logical and comparison operators

a = 6
b = 9

# Write your code below

if a % 2 == 0 and b % 2 == 0:
    print("BOTH EVEN")
elif a % 2 != 0 and b % 2 != 0:
    print("BOTH ODD")
else:
    print("ONE EVEN ONE ODD")

print(a^ b)