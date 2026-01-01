# ============================================================
#               PYTHON CONDITIONALS (IF / ELIF / ELSE)
# ============================================================

# Conditional statements let your program make decisions.
# Python checks conditions from TOP to BOTTOM.

# -------------------------
# 1️⃣ Basic IF statement
# -------------------------

age = 20

if age >= 18 :
    print("You are Adult")

# -------------------------
# 2️⃣ IF–ELSE
# -------------------------

marks = 40
if marks >= 50:
   print("Pass")
else :
  print("Fail")

# -------------------------
# 3️⃣ IF–ELIF–ELSE
# -------------------------

score = 72

if score >= 90:
   print("Grade A")
elif score >=75:
   print("Grade B")
elif score >= 60:
   print("Grade C")
else:
   print("Grade D")

# -------------------------
# 4️⃣ Nested IF
# -------------------------

num = 12

if num > 0:
   print("Positive number")
   if num % 2 == 0:
      print("Even number")
else:
   print("Negative Number")      

# -------------------------
# 5️⃣ Multiple Conditions (AND / OR)
# -------------------------

height = 100 
weight = 75

if height > 50 and weight < 100:
   print("Both conditions matched")

if height > 50 or weight < 100:
   print("At Least One condition matches")

# -------------------------
# 6️⃣ Conditional Expression (Ternary Operator)
# -------------------------

x = 10
y = 12

larger = x if x > y else y
print("Larger number is: ", larger)

# ============================================================
#                      PRACTICE PROBLEMS
# ============================================================

# Problem 1:
# Take a number stored in num_a.
# Print:
# - "Positive" if > 0
# - "Negative" if < 0
# - "Zero" if == 0

num_a = 15   # change values while testing

if num_a > 0:
   print("Positive")
elif num_a < 0:
   print("Negative")
else:
   print("Zero")

# Problem 2:
# Take age_b.
# Print "Teenager" if age_b is between 13 and 19 (inclusive).
# Else print "Not a teenager".

age_b = 17

if 13 <= age_b <= 19:
   print("Teenager")
else:
   print("Not a teenager")

# Problem 3:
# Given score_c:
# - 90+ → "Excellent"
# - 75–89 → "Good"
# - 50–74 → "Average"
# - else → "Poor"

score_c = 68

if score_c >= 90:
   print("Excellent")
elif 75 <= score_c <= 89:
    print("Good")
elif 50 <= score_c <= 74:
    print("Average")
else:
   print("Poor")

# Problem 4:
# Check if a number num_d is EVEN or ODD using modulo.

num_d = 51

if num_d % 2 == 0:
   print("Even")
else:
   print("Odd")

# Problem 5:
# Use nested conditions:
# Given num_e:
# If num_e > 0:
#       If even → print "Positive Even"
#       Else → print "Positive Odd"
# Else:
#       print "Non-positive"

num_e = 12

if num_e > 0:
   if num_e % 2 == 0:
      print("Positive Even")
   else:
      print("Positive Odd")
else:
   print("Non-positive")

# Problem 6:
# Using AND:
# Given temp_f and humid_f:
# Print "Weather OK" if:
#       temp_f between 20–30 AND humid_f below 60

temp_f = 28
humid_f = 45

if  20 <= temp_f <= 30 and humid_f < 60:
   print("Weather OK")

# Problem 7:
# Using OR:
# Given speed_g:
# Print "Warning!" if:
#       speed_g < 20 OR speed_g > 120

speed_g = 15

if speed_g < 20 or speed_g > 120:
   print("Warning!")

# Problem 8:
# Ternary operator:
# Given n1_h and n2_h:
# Print the larger number.

n1_h = 54
n2_h = 98

larger = n1_h if n1_h > n2_h else n2_h
print("Larger: ", larger)

# Problem 9:
# Ask the user to input a number. 
# Print "Positive" if it is greater than 0, "Negative" if it is less than 0, or "Zero" if it is 0.

num = int(input("Enter a number: "))
if num > 0:
   print("Positive")
elif num < 0:
   print("Negative")
else:
   print("Zero")

# Problem 10:
# Ask the user to input their age.
# Print "Senior" if age >= 60, "Adult" if age is between 18 and 59, or "Minor" if less than 18.

age = int(input("Enter your age: "))
if age >= 60:
   print("Senior")
elif 18 <= age <= 59:
   print("Adult")
else:
   print("Minor")

# Problem 11:
# Ask the user to input a number.
# If the number is divisible by both 3 and 5, print "FizzBuzz".
# If divisible by only 3, print "Fizz".
# If divisible by only 5, print "Buzz".
# Otherwise, print "None".

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
   print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
   print("None")
      
# Problem 12:
# Ask the user to input the current temperature.
# Print "Hot" if temperature > 35,
# "Warm" if temperature is between 20 and 35,
# "Cool" if temperature is between 10 and 19,
# or "Cold" if temperature < 10.

temp = int(input("Input the current temperature: "))
if temp > 35:
   print("Hot")
elif 20 <= temp <= 35:
   print("Warm")
elif 10 <= temp <= 19:
   print("Cool")
else:
   print("Cold")

# Problem 13:
# Ask the user to input a number.
# If the number is greater than 100:
#   If it is even, print "Big Even".
#   If it is odd, print "Big Odd".
# Else, print "Small Number".

num = int(input("Enter a number: "))
if num > 100:
   if num % 2 == 0:
      print("Big Even")
   else:
      print("Big Odd")
else:
   print("Small Number")

# Problem 14:
# Ask the user to input their salary and years of experience.
# Print "Eligible" if salary >= 30000 AND experience >= 2, otherwise print "Not eligible".

salary = int(input("Enter your salary: "))
experience = int(input("Enter years of experience: "))
if salary >= 30000 and experience >= 2:
   print("Eligible")
else:
   print("Not eligible")

# Problem 15:
# Ask the user to input the traffic light color.
# Print "Stop!" if it is "red" or "yellow", otherwise print "Go".

light_color = input("Enter traffic light color: ")
light_color_lower = light_color.lower()
if light_color_lower == "red" or light_color_lower == "yellow":
   print("Stop!")
else:
   print("Go")

# Problem 16:
# Ask the user to input two numbers.
# Use a conditional expression to print the smaller of the two numbers.

a, b = map(int, input("Enter two number: ").split())
if a < b:
   print(a)
else:
   print(b)

# Problem 17:
# Ask the user to input three numbers.
# Print the largest number among them.

a, b, c = map(int, input("Enter three numbers: ").split())
if a >= b and a >= c:
   print(a)
elif  b >= a and b >= c:
   print(b)
else:
   print(c)

# Problem 18:
# Ask the user to input three numbers.
# Print them in descending order.

num = map(int, input("Enter three numbers: ").split())
num_descending = sorted(num)[::-1]
print(f"Descending order: {num_descending}")

# Problem 19:
# Ask the user to input a year.
# Print "Leap year" if it is a leap year, otherwise print "Not a leap year".
# (Leap year: divisible by 4 and not by 100, or divisible by 400)

year = int(input("Input a year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
   print("Leap year")
else:
   print("Not a leap year")

# Problem 20:
# Ask the user to input a number.
# Print "Prime" if the number is prime, otherwise print "Not prime".

num = int(input("Enter a number: "))

if num < 2:
   print("Not prime")
else:
   is_prime = True
   for i in range(2, num):
      if num % i == 0:
         is_prime = False
         break
      
   if is_prime:
         print("Prime")
   else:
         print("Not prime")


# Problem 21:
# Ask the user to input a character.
# Print "Vowel" if it is a vowel, otherwise print "Consonant".

char = input("Enter a character: ")
char_lower = char.lower()
if char_lower in "aeiou":
   print("vowel")
else:
   print("Consonant")

# Problem 22:
# Ask the user to input a number.
# Print "Palindrome" if the number reads the same forwards and backwards, else print "Not palindrome".

num = input("Enter a number: ")
num_reverse = num[::-1]
if  num == num_reverse:
   print("Palindrome")
else:
   print("Not palindrome")

# Problem 23:
# Ask the user to input three exam scores.
# Print the corresponding grade:
#   Average >= 90 → "A"
#   Average >= 75 → "B"
#   Average >= 60 → "C"
#   Else → "D"

a, b, c = map(int, input("Enter three exam scores: ").split())
average = (a + b + c) / 3
if average >= 90:
   print("A")
elif average >= 75:
   print("B")
elif average >= 60:
   print("C")
else:
   print("D")

# Problem 24:
# Ask the user to input an integer.
# Print whether it is divisible by 2, 3, 5, or none of them.

integer = int(input("Enter an integer: "))
if integer % 2 == 0:
   print("Divisible by 2")
elif integer % 3 == 0:
   print("Divisible by 3")
elif integer % 5 == 0:
   print("Divisible by 5")
else:
   print("None of these")

# Problem 25:
# Ask the user to input three numbers.
# Print the largest number among them.

a, b, c = map(int, input("Enter three numbers: ").split())
if a >= b and a >= c:
   print(a) 
elif b >= a and b >= c:
   print(b)
else:
   print(c)

# Problem 26:
# Ask the user to input two numbers.
# Print "Equal" if both are same,
# otherwise print which one is greater.

a, b = map(int, input("Enter two numbers: ").split())
if a == b:
   print("Equal")
elif a > b:
   print(a)
else:
   print(b)

# Problem 27:
# Ask the user to input a character.
# Print "Vowel" if it is a vowel (a, e, i, o, u),
# otherwise print "Consonant".

char = input("Enter a character: ")
char_lower = char.lower()
if char_lower in "aeiou":
   print("Vowel")
else:
   print("Consonant")

# Problem 28:
# Ask the user to input a number.
# If the number is positive → print "Positive".
# If negative → print "Negative".
# If zero → print "Zero".

num = int(input("Enter a number: "))
if num > 0:
   print("Positive")
elif num < 0:
   print("Negative")
else:
   print("Zero")   

# Problem 29:
# Ask the user to input a year.
# Print "Leap Year" or "Not Leap Year"
# using correct leap year rules.

year = int(input("Enter a year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
   print("Leap year")
else:
   print("Not Leap Year")

# Problem 30:
# Ask the user to input two integers.
# Print:
#   "Both Even" if both are even.
#   "Both Odd" if both are odd.
#   "Mixed" otherwise.

a, b = map(int, input("Enter two integers: ").split())
if a % 2 == 0 and b % 2 == 0:
   print("Both Even")
elif a % 2 != 0 and b % 2 != 0:
   print("Both Odd")
else:
   print("Mixed")

# Problem 31:
# Ask the user to input age.
# If age < 13 → print "Child"
# 13–19 → print "Teen"
# 20+ → print "Adult".

age = int(input("Enter age: "))
if age < 13:
   print("Child")
elif 13 <= age <= 19:
   print("Teen")
else:
   print("Adult")

# Problem 32:
# Ask the user to input a number.
# If number has 1 digit → print "One digit"
# If 2 digits → print "Two digits"
# If 3 digits → print "Three digits"
# Otherwise → print "More than three digits"
# (No loops allowed.)

num = input("Enter a number: ")
num_length = len(num)

if num_length == 1:
   print("One digit")
elif num_length == 2:
   print("Two digits")
elif num_length == 3:
   print("Three digits")
else:
   print("More than three digits")

# Problem 33:
# Ask the user to input a number.
# If divisible by 7 → print "Lucky"
# Otherwise → print "Unlucky".

num = int(input("Enter a number: "))
if num % 7 == 0:
   print("Lucky")
else:
   print("Unlucky")

# Problem 34:
# Ask the user to input a letter.
# Print "Uppercase" if it's uppercase,
# "Lowercase" if lowercase,
# else print "Not a letter".

letter = input("Enter a letter: ")

if letter.isalpha():
   if letter.isupper():
      print("Uppercase")
   else:
      print("Lowercase")
else:
   print("Not a letter")

# Problem 35:
# Ask the user to input two numbers.
# Print "Same sign" if both positive or both negative.
# Print "Opposite sign" otherwise.

a, b = map(int, input("Enter two numbers: ").split())
if a > 0 and b > 0 or a < 0 and b < 0:
   print("Same sign")
else:
   print("Opposite sign")

   # Problem 36:
# Ask the user to input a number.
# Print "Multiple of 5" if divisible by 5,
# "Multiple of 3" if divisible by 3,
# "Multiple of 15" if divisible by both 3 and 5,
# Otherwise print "None".

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
   print("Multiple of 15")
elif num % 5 == 0:
   print("Multiple of 5")
elif num % 3 == 0:
   print("Multiple of 3")
else:
   print("None")

# Problem 37:
# Ask the user to input a number.
# Print "Negative and Even" if the number is negative and even,
# "Negative and Odd" if negative and odd,
# "Positive" if positive,
# "Zero" if zero.

num = int(input("Enter a number: "))
if num < 0 and num % 2 == 0:
   print("Negative and Even")
elif num < 0 and num % 2 != 0:
   print("Negative and Odd")
elif num > 0:
   print("Positive")
else:
   print("Zero")
 
# Problem 38:
# Ask the user to input three numbers.
# Print them in ascending order.

num = map(int, input("Enter three numbers: ").split())
num_ascending = sorted(num)
print(f"Numbers in ascending: {num_ascending}")

# Problem 39:
# Ask the user to input a character.
# Print "Digit" if it is a number,
# "Alphabet" if a letter,
# "Other" otherwise.

char = input("Enter a character: ")
if char in "0123456789":
   print("Digit")
elif char.isalpha():
   print("Alphabet")
else:
   print("Other")

# Problem 40:
# Ask the user to input two numbers.
# Print "One positive, one negative" if one number is positive and the other negative,
# Print "Both positive" if both positive,
# Print "Both negative" if both negative,
# Otherwise print "Zero involved".

a, b = map(int, input("Enter two numbers: "))
if a > 0  and b > 0:
   print("Both positive")
elif a < 0 and b < 0:
   print("Both negative")
elif a > 0 and b < 0 or a < 0 and b > 0:
   print("One positive, one negative")
else:
   print("Zero involved")