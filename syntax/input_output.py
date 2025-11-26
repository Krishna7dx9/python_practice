## ------------------------------------------------------------
## 1. Basic input and output
## ------------------------------------------------------------
#
## input() always returns a STRING
#name = input("Enter your name: ")
#
## Using f-string to format output
#print(f"Hello, {name}!")
#
## ------------------------------------------------------------
## 2. Take two numbers and print their sum
## ------------------------------------------------------------
#
## Convert input from string → int
#num1 = int(input("Enter first number: "))
#num2 = int(input("Enter second number: "))
#
## Calculate sum 
#total = num1 + num2
#
## Output result 
#print(f"The sum of {num1} and {num2} is {total}")
#
## ------------------------------------------------------------
## 3. Age check (Adult / Minor)
## ------------------------------------------------------------
#
#age = int(input("Enter age: "))
#
## Simple condition
#if age >= 18:
#    print("Adult")
#else:
#    print("Minor")
#
## ------------------------------------------------------------
## 4. Three numbers → max, min, average
## ------------------------------------------------------------
#
## Take 3 inputs in one line, separated by space
## Example input: 10 20 30
#a, b, c = map(int, input("Enter three numbers: ").split())
#
## Compute results
#maximum = max(a, b, c)
#minimum = min(a, b, c)
#average = (a + b + c) / 3
#
## Print results clearly
#print(f"Max: {maximum}")
#print(f"Minimum: {minimum}")
#print(f"Average: {average}")
#
## ------------------------------------------------------------
## 5. List of numbers in one line → convert to Python list
## ------------------------------------------------------------
#
## Ask user to input numbers separated by spaces
## Example: 5 10 2 9 26
#numbers_str = input("Enter numbers separated by space: ").split()
#
## Convert each number from string → int 
#numbers = [int(x) for x in numbers_str]
#
## Output clean list
#print(f"Your List: {numbers}")


## ------------------------------------------------------------
## 1. Take user's full name and print:
##    - First name
##    - Last name
##    - Length of full name (excluding spaces)
## Example:
## Input: "Kris Sharma"
## Output:
## First name: Kris
## Last name: Sharma
## Length: 10
## ------------------------------------------------------------
#
#first_name, last_name = map(str, input("Enter your Full Name: ").split())
#
#print(f"First Name: {first_name})")
#print(f"Last Name: {last_name}")
#print(len(first_name + last_name))
#
## ------------------------------------------------------------
## 2. Ask user for two integers.
##    Print:
##    - Their sum
##    - Their difference
##    - Their product
##    - Their integer division result (num1 // num2)
## ------------------------------------------------------------
#
#a, b = map(int, input("Enter two numbers seprated by space: ").split())
#
#print(f"Sum: {a + b}")
#print(f"Difference: {a - b}")
#print(f"Product: {a * b}")
#print(f"Integer Division: {a // b}")
#
## ------------------------------------------------------------
## 3. Take three space-separated floats.
##    Print:
##    - Largest value
##    - Smallest value
##    - Rounded average (round to 2 decimal places)
## ------------------------------------------------------------
#
#num1, num2, num3 = map(float, input("Enter Tree space seprated floats: ").split())
#
#print(max(num1, num2, num3))
#print(min(num1, num2, num3))
#average = (num1 + num2 + num3)/3
#rounded_average = round(average)
#print(rounded_average)

# ------------------------------------------------------------
# 4. Take comma-separated numbers.
#    Convert them into a list of integers.
#    Print:
#    - The list
#    - The number of even numbers
#    - The number of odd numbers
# Example:
# Input: "1,2,3,4,5"
# ------------------------------------------------------------

the_list = list(str(input("Enter comma seprated numbers: ")))
the_list = int(the_list)
print(the_list)


# ------------------------------------------------------------
# 5. Ask user for a sentence.
#    Print:
#    - Number of words
#    - Number of characters (excluding spaces)
#    - Sentence reversed
# ------------------------------------------------------------
