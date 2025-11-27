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
#print(f"First Name: {first_name}")
#print(f"Last Name: {last_name}")
#print(f"Full name length: {len(first_name + last_name)}")
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
#num1, num2, num3 = map(float, input("Enter Three space seprated floats: ").split())
#
#print(max(num1, num2, num3))
#print(min(num1, num2, num3))
#average = (num1 + num2 + num3)/3
#rounded_average = round(average, 2)
#print(rounded_average)
#
## ------------------------------------------------------------
## 4. Take comma-separated numbers.
##    Convert them into a list of integers.
##    Print:
##    - The list
##    - The number of even numbers
##    - The number of odd numbers
## Example:
## Input: "1,2,3,4,5"
## ------------------------------------------------------------
#
#the_list = input("Enter Comma seprated numbers: ")
#the_list = the_list.split(",")
#the_list = [int(x) for x in the_list]
#
#print(the_list)
#
#even_count = sum(1 for x in the_list if x % 2 == 0)
#odd_count = sum(1 for x in the_list if x % 2 != 0)
#
#print(even_count)
#print(odd_count)
#
## ------------------------------------------------------------
## 5. Ask user for a sentence.
##    Print:
##    - Number of words
##    - Number of characters (excluding spaces)
##    - Sentence reversed
## ------------------------------------------------------------
#
#sentence = input("Enter a sentence: ")
#words = len(sentence.split())
#no_of_char = len(sentence.replace(" ", ""))
#reversed_sentence = sentence[::-1]
#
#print(words)
#print(no_of_char)
#print(reversed_sentence)

# ------------------------------------------------------------
# 6. Take a full name (any number of words).
#    Print:
#    - First word
#    - Last word
#    - Total characters excluding spaces
# ------------------------------------------------------------

the_full_name = input("Enter full Name: ")

words_of_the_full_name = the_full_name.split()
first_word = words_of_the_full_name[0]
last_word =  words_of_the_full_name[-1]
chr_exclude_space = len(the_full_name.replace(" ", ""))

print(f"First word: {first_word}")
print(f"Last word: {last_word}")
print(f"Characters excluding space: {chr_exclude_space}")

# ------------------------------------------------------------
# 7. Ask for three integers.
#    Print:
#    - Sum
#    - Average (rounded to 1 decimal)
#    - Product
# ------------------------------------------------------------

three_integer = list(map(int, input("Enter three intergers: ").split()))

sum_of_three_integer = sum(three_integer)
average = (sum_of_three_integer / 3)
average_rounded = round(average, 1)
product = 1
for x in three_integer:
    product *= x


print(f"Sum: {sum_of_three_integer}")
print(f"Average Rounded: {average_rounded}")
print(product)

# ------------------------------------------------------------
# 8. Take space-separated words.
#    Print:
#    - Number of words
#    - Longest word
#    - Shortest word
# ------------------------------------------------------------

enter_words = input("Enter space seprated words: ")
words_count = len(enter_words)
longest_word = max(enter_words, key = len)
shortest_word = min(enter_words, key = len)

print(f"Number of words: {enter_words}")
print(longest_word)
print(shortest_word) 

# ------------------------------------------------------------
# 9. Take comma-separated integers.
#    Print:
#    - The list
#    - Maximum number
#    - Minimum number
#    - Difference between max and min
# ------------------------------------------------------------

comma_seprated = input("Enter comma Seprated integers: ").split()
comma_seprated = int(comma_seprated)
maximum_num = max(comma_seprated)
minimum_num = min(comma_seprated)
difference_max_min = maximum_num - minimum_num

print(f"The comma seprated list: {comma_seprated}")
print(f"Maximum numbers: {maximum_num}")
print(f"Minimum_num: {minimum_num}")
print(f"Difference of max min: {difference_max_min}")

# ------------------------------------------------------------
# 10. Take a sentence.
#     Print:
#     - Characters including spaces
#     - Characters excluding spaces
#     - Words reversed order (not characters)
#       Example: "I love Python" → "Python love I"
# ------------------------------------------------------------

enter_sentence = input("Enter a sentence: ")
char_excluding_spaces = enter_sentence.split(" ")

words_ = enter_sentence.split()
words_reversed = words_[-1]

print(enter_sentence)
print(char_excluding_spaces)
print(words_reversed)