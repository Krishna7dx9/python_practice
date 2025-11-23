# ------------------------------------------------------------
# 1. Basic input and output
# ------------------------------------------------------------

# input() always returns a STRING
name = input("Enter your name: ")

# Using f-string to format output
print(f"Hello, {name}!")

# ------------------------------------------------------------
# 2. Take two numbers and print their sum
# ------------------------------------------------------------

# Convert input from string → int
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate sum 
total = num1 + num2

# Output result 
print(f"The sum of {num1} and {num2} is {total}")

# ------------------------------------------------------------
# 3. Age check (Adult / Minor)
# ------------------------------------------------------------

age = int(input("Enter age: "))

# Simple condition
if age >= 18:
    print("Adult")
else:
    print("Minor")

# ------------------------------------------------------------
# 4. Three numbers → max, min, average
# ------------------------------------------------------------

# Take 3 inputs in one line, separated by space
# Example input: 10 20 30
a, b, c = map(int, input("Enter three numbers: ").split())

# Compute results
maximum = max(a, b, c)
minimum = min(a, b, c)
average = (a + b + c) / 3

# Print results clearly
print(f"Max: {maximum}")
print(f"Minimum: {minimum}")
print(f"Average: {average}")

# ------------------------------------------------------------
# 5. List of numbers in one line → convert to Python list
# ------------------------------------------------------------

# Ask user to input numbers separated by spaces
# Example: 5 10 2 9 26
numbers_str = input("Enter numbers separated by space: ").split()

# Convert each number from string → int 
numbers = [int(x) for x in numbers_str]

# Output clean list
print(f"Your List: {numbers}")