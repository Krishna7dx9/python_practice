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


# ------------------------------------------------------------
# 1. Take user's full name and print:
#    - First name
#    - Last name
#    - Length of full name (excluding spaces)
# Example:
# Input: "Kris Sharma"
# Output:
# First name: Kris
# Last name: Sharma
# Length: 10
# ------------------------------------------------------------

first_name, last_name = map(str, input("Enter your Full Name: ").split())

print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Full name length: {len(first_name + last_name)}")

# ------------------------------------------------------------
# 2. Ask user for two integers.
#    Print:
#    - Their sum
#    - Their difference
#    - Their product
#    - Their integer division result (num1 // num2)
# ------------------------------------------------------------

a, b = map(int, input("Enter two numbers seprated by space: ").split())

print(f"Sum: {a + b}")
print(f"Difference: {a - b}")
print(f"Product: {a * b}")
print(f"Integer Division: {a // b}")

# ------------------------------------------------------------
# 3. Take three space-separated floats.
#    Print:
#    - Largest value
#    - Smallest value
#    - Rounded average (round to 2 decimal places)
# ------------------------------------------------------------

num1, num2, num3 = map(float, input("Enter Three space seprated floats: ").split())

print(max(num1, num2, num3))
print(min(num1, num2, num3))
average = (num1 + num2 + num3)/3
rounded_average = round(average, 2)
print(rounded_average)

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

the_list = input("Enter Comma seprated numbers: ")
the_list = the_list.split(",")
the_list = [int(x) for x in the_list]

print(the_list)

even_count = sum(1 for x in the_list if x % 2 == 0)
odd_count = sum(1 for x in the_list if x % 2 != 0)

print(even_count)
print(odd_count)

# ------------------------------------------------------------
# 5. Ask user for a sentence.
#    Print:
#    - Number of words
#    - Number of characters (excluding spaces)
#    - Sentence reversed
# ------------------------------------------------------------

sentence = input("Enter a sentence: ")
words = len(sentence.split())
no_of_char = len(sentence.replace(" ", ""))
reversed_sentence = sentence[::-1]

print(words)
print(no_of_char)
print(reversed_sentence)

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

enter_words = input("Enter space seprated words: ").split()
words_count = len(enter_words)
longest_word = max(enter_words, key = len)
shortest_word = min(enter_words, key = len)

print(f"Number of words: {words_count}")
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

comma_seprated = list(map(int, input("Enter comma Seprated integers: ").split(",")))
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
char_spaces = len(enter_sentence)
char_excluding_spaces = len(enter_sentence.replace(" ", ""))
words_reversed = " ".join(enter_sentence.split()[::-1])

print(f"Characters including spaces: {char_spaces}")
print(f"Characters excluding spaces: {char_excluding_spaces}")
print(f"Words reversed order: {words_reversed}")

# ------------------------------------------------------------
# 11. Ask user for two floating-point numbers.
#     Print:
#     - Their sum
#     - Their difference
#     - Their product
#     - Their division (rounded to 2 decimals)
# ------------------------------------------------------------

# Your code here

a, b  = map(float, input("Enter two floating point number: ").split())

sum_ = a + b
difference_ = a - b
product_ = a * b
division_ = a / b
rounded_division_ = round(division_, 2)

print(f"Sum: {sum_}")
print(f"Difference: {difference_}")
print(f"Product: {product_}")
print(f"Rounded Division: {rounded_division_}")

# ------------------------------------------------------------
# 12. Take a list of space-separated integers from the user.
#     Print:
#     - The list sorted in ascending order
#     - The list sorted in descending order
#     - The sum of all numbers
# ------------------------------------------------------------

# Your code here

integers = list(map(int, input("Enter space seprated integers: ").split()))
ascending_sort = sorted(integers)
decending_sort = sorted(integers)[::-1]
sum_ = sum(integers) 

print(f"Ascending Sorted: {ascending_sort}")
print(f"Decending Sorted: {decending_sort}")
print(f"Sum: {sum_}")

# ------------------------------------------------------------
# 13. Ask user for a sentence.
#     Print:
#     - Number of vowels (a, e, i, o, u)
#     - Number of consonants
#     - Number of digits
#     - Number of special characters (anything not letter or digit)
# ------------------------------------------------------------

# Your code here

sentence_ = input("Enter a sentence: ")
sentence_lower = sentence_.lower()
vowel = 0
for x in sentence_lower:
    if x in "aeiou":
        vowel += 1
consonant = 0
for x in sentence_lower:
    if x.isalpha() and x not in "aeiou":
        consonant += 1
digit_ = 0
for x in sentence_:
    if x in "1234567890":
        digit_ += 1
special_char = 0
for x in sentence_:
    if not x.isalnum():
        special_char += 1

print(f"Number of vowels: {vowel}")
print(f"Number of consonant: {consonant}")
print(f"Number of digit_: {digit_}")
print(f"Number of special charracters: {special_char}")

# ------------------------------------------------------------
# 14. Ask user for a word.
#     Print:
#     - The word in uppercase
#     - The word in lowercase
#     - The word reversed
# ------------------------------------------------------------

# Your code here

word = input("Enter a word: ")
word_upper = word.upper()
word_lower = word.lower()
word_reversed = word[::-1]

print(word_upper)
print(word_lower)
print(word_reversed)

# ------------------------------------------------------------
# 15. Ask user for a string of comma-separated words.
#     Print:
#     - The list of words
#     - The number of words
#     - The longest word
#     - The shortest word
# ------------------------------------------------------------

# Your code here

input_words = input("Enter comma seprated words: ")
list_words = list(input_words.split(","))
length_words = len(list_words)
longest_word = max(list_words, key = len)
shortest_word = min(list_words, key = len)

print(f"List of words: {list_words}")
print(f"Number of words: {length_words}")
print(f"Longest word: {longest_word}")
print(f"Shortest word: {shortest_word}")

# ------------------------------------------------------------
# 16. Ask user for a list of integers (space-separated).
#     Print:
#     - The even numbers
#     - The odd numbers
#     - Count of even numbers
#     - Count of odd numbers
# ------------------------------------------------------------

integers = list(map(int, input("Enter space seprated integers: ").split()))
even_numbers = []
for x in integers:
    if x % 2 == 0:
        even_numbers.append(x)
odd_numbers = []
for x in integers:
    if x % 2 != 0:
        odd_numbers.append(x)
count_even = len(even_numbers)
count_odd = len(odd_numbers)

print(f"Even numbers: {even_numbers}")
print(f"Odd Numbers: {odd_numbers}")
print(f"Count even number: {count_even}")
print(f"Count odd number: {count_odd}")

# ------------------------------------------------------------
# 17. Ask user for a sentence.
#     Print:
#     - The sentence in uppercase
#     - The sentence in lowercase
#     - The number of words
# ------------------------------------------------------------

sentence = input("Enter a sentence: ")
sentence_upper = sentence.upper()
sentence_lower = sentence.lower()
no_of_words = len(sentence.split())

print(f"Sentence in uppercase: {sentence_upper}")
print(f"Sentence lowercase: {sentence_lower}")
print(f"Number of words: {no_of_words}")

# ------------------------------------------------------------
# 18. Ask user for a list of integers (comma-separated).
#     Print:
#     - The list
#     - Only the positive numbers
#     - Only the negative numbers
#     - Count of zeroes
# ------------------------------------------------------------

integers = list(map(int, input("Enter integers comma seprated: ").split(",")))
positive = []
for x in integers:
    if x > 0:
        positive.append(x)
negative = []
for x in integers:
    if x < 0:
        negative.append(x)
zeros = []
for x in integers:
    if x == 0:
        zeros.append(x)

# ------------------------------------------------------------
# 19. Take a word from the user.
#     Print:
#     - Whether it is a palindrome (same forward & backward)
#     - Its length
# ------------------------------------------------------------

word = input("Enter a word: ")
word_reverse = word[::-1]
if word == word_reverse:
    print(f"The word {word} is Palindrome")
else:
    print("Not palindrome")
length_word = len(word)

print(f"Length of {word}: {length_word}")

# ------------------------------------------------------------
# 20. Ask user for space-separated names.
#     Print:
#     - Names sorted alphabetically
#     - Names sorted in reverse alphabetical order
#     - Total number of names
# ------------------------------------------------------------

names = input("Enter space seprated names: ").split()
names_sorted = sorted(names)
names_sorted_reverse = sorted(names)[::-1]
total_names = len(names)

print(f"Names sorted: {names_sorted}")
print(f"Reversed names sorted: {names_sorted_reverse}")
print(f"Total names: {total_names}")

# ------------------------------------------------------------
# 21. Ask the user for a string.
#     Count and print:
#     - Number of digits
#     - Number of alphabets
#     - Number of spaces
#     - Number of special characters (anything not letter/digit/space)
# ------------------------------------------------------------

# Your code here

enter_str = input("Enter a string: ")
no_of_digit = 0
for x in enter_str:
    if x in "0123456789":
        no_of_digit += 1
no_of_alpha = 0
for x in enter_str:
    if x.isalpha():
        no_of_alpha += 1
no_of_spaces = 0
for x in enter_str:
    if x == " ":
        no_of_spaces += 1
no_of_special = 0
for x in enter_str:
    if not x.isalnum():
        no_of_special += 1

print(f"Number of digits: {no_of_digit}")
print(f"Number of alphabets: {no_of_alpha}")
print(f"Number of spaces: {no_of_spaces}")
print(f"Number of special characters: {no_of_special}")

# ------------------------------------------------------------
# 22. Ask the user for a list of space-separated integers.
#     Print:
#     - Maximum number
#     - Minimum number
#     - Difference between max and min
# ------------------------------------------------------------

# Your code here

integers = list(map(int, input("Enter space seprated integers: ").split()))
maximum = max(integers)
minimum = min(integers)
difference = maximum - minimum

print(f"Maximum number: {maximum}")
print(f"Minimum number: {minimum}")
print(f"Difference: {difference}")

# ------------------------------------------------------------
# 23. Ask the user for a sentence.
#     Print:
#     - All words in reverse order
#     - All words sorted alphabetically
# ------------------------------------------------------------

# Your code here

sentence = input("Enter a sentence: ")
words = sentence.split()
words_reversed = words[::-1]
words_sorted = sorted(words)

print(words_reversed)
print(words_sorted)

# ------------------------------------------------------------
# 24. Ask the user for a sentence.
#     Print:
#     - Number of vowels
#     - Number of consonants
#     - Number of digits
#     - Number of special characters
# ------------------------------------------------------------

# Your code here

sentence = input("Enter a sentence: ")
sentence_lower = sentence.lower()
vowels_count = 0
for x in sentence_lower:
    if x in "aeiou":
        vowels_count += 1
consonants_count = 0
for x in sentence_lower:
    if x.isalpha() and x not in "aeiou":
        consonants_count += 1
digits_count = 0
for x in sentence_lower:
    if  x in "0123456789":
        digits_count += 1
special_char_count = 0
for x in sentence_lower:
    if not x.isalnum():
        special_char_count +=1
print(f"Number of vowels: {vowels_count}")
print(f"Number of consonants: {consonants_count}")
print(f"Number of digit: {digits_count}")
print(f"Number of special characters count: {special_char_count}")

# ------------------------------------------------------------
# 25. Ask the user for a string.
#     Print:
#     - The string in uppercase
#     - The string in lowercase
#     - The string reversed
# ------------------------------------------------------------

# Your code here

a_string = input("Enter a string: ")
string_upper = a_string.upper()
string_lower = a_string.lower()
string_reversed = a_string[::-1]

print(f"String uppercase: {string_upper}")
print(f"String lowercase: {string_lower}")
print(f"String reversed: {string_reversed}")