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