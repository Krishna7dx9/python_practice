# ============================================================
# FUNCTIONS IN PYTHON — COMPLETE SYNTAX
# ============================================================

# ------------------------------------------------------------
# 1. Basic function definition
# ------------------------------------------------------------
# A function is created using `def`
# It only runs when you CALL it.

def greet():
    print("Hello from a function!")

# ------------------------------------------------------------
# 2. Function with parameters
# ------------------------------------------------------------
# Parameters = values you PASS into a function

def greet_person(name):
    print(f"Hello, {name}!")

# ------------------------------------------------------------
# 3. Function with TWO parameters
# ------------------------------------------------------------

def add_number(a, b):
    return a + b             # return sends value OUT of function

# ------------------------------------------------------------
# 4. Function with a DEFAULT parameter
# ------------------------------------------------------------
# If no value is passed → default value is used

def welcome(user="Guest"):
    print(f"Welcome, {user}!")

# ------------------------------------------------------------
# 5. Function returning MULTIPLE values
# ------------------------------------------------------------
# Python returns multiple values as a tuple

def math_operations(x, y):
    add = x + y
    sub = x - y
    mul = x * y
    return add, sub, mul

# ------------------------------------------------------------
# 6. Keyword arguments
# ------------------------------------------------------------
# You can pass arguments by name

def user_info(name, age):
    print(f"Name: {name}, Age: {age}")

# user_info(age=30, name="Kris")
# Order doesn’t matter when key=value is used

# ------------------------------------------------------------
# 7. Arbitrary arguments (*args → multiple values)
# ------------------------------------------------------------
# When you don’t know how many arguments the user will pass

def sum_all(*nums):
    total = 0
    for n in nums:
        total += n
    return total

# ------------------------------------------------------------
# 8. Arbitrary keyword arguments (**kwargs)
# ------------------------------------------------------------
# Accepts unlimited key=value pairs

def print_details(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

# ------------------------------------------------------------
# 9. Function inside a function (Nested functions)
# ------------------------------------------------------------

def outer():
    def inner():
        return  "Inside inner functions"
    return inner()

# ------------------------------------------------------------
# 10. Lambda functions (one-line SMALL functions)
# ------------------------------------------------------------

square_ = lambda x: x * x
add_lambda = lambda a, b: a + b

# ------------------------------------------------------------
# Problem 1:
# Create a function called say_hello that:
# - takes a name
# - prints "Hello, <name>!"
# ------------------------------------------------------------

def say_hello(name):
    print(f"Hello, {name}!")

# ------------------------------------------------------------
# Problem 2:
# Create a function multiply_three that:
# - takes 3 numbers
# - returns their product
# ------------------------------------------------------------

def multiply_three(g, h, j):
    product =  g * h * j
    return product

# ------------------------------------------------------------
# Problem 3:
# Create a function describe_person with:
# - 2 parameters: person_name, city
# - prints: "<person_name> lives in <city>"
# ------------------------------------------------------------

def describe_person(person_name, city):
    print(f"{person_name} lives in {city}")

# ------------------------------------------------------------
# Problem 4:
# Create a function called find_stats that:
# - takes a list of numbers
# - returns (max, min, sum)
# ------------------------------------------------------------

def find_stats(numbers):
    return max(numbers), min(numbers), sum(numbers)

# ------------------------------------------------------------
# Problem 5:
# Create a function bonus_points with DEFAULT parameter:
# - takes score and bonus=10
# - returns score + bonus
# ------------------------------------------------------------

def bonus_points(score, bonus = 10):
    return score + bonus

# ------------------------------------------------------------
# Problem 6:
# Create sum_any function using *args that:
# - accepts ANY number of integers
# - returns the total
# ------------------------------------------------------------

def sum_any(*nums):
    total = 0
    for n in nums:
       total += n
    return total

# ------------------------------------------------------------
# Problem 7:
# Create a function show_profile using **kwargs
# - print all key:value pairs
# Example:
#     show_profile(name="Kris", age=21, skill="Python")
# ------------------------------------------------------------

def show_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

# ------------------------------------------------------------
# Problem 8:
# Write a lambda function:
# - input: a number
# - output: number squared
# Store it in: square_num
# ------------------------------------------------------------

square_num = lambda num_a: num_a * num_a

# ------------------------------------------------------------
# Problem 9:
# Create a function called greet_users that:
# - takes a list of names
# - prints "Hello, <name>!" for each name
# Example: greet_users(["Kris","Alex"]) → prints:
# Hello, Kris!
# Hello, Alex!
# ------------------------------------------------------------

# Write your code below
def greet_users(names):
        for name in names:
            print(f"Hello, {name}!")

# ------------------------------------------------------------
# Problem 10:
# Create a function calculate_power that:
# - takes 2 numbers: base and exponent
# - returns base ** exponent
# ------------------------------------------------------------

# Write your code below

def calculate_power(base, exponent):
    return base ** exponent

# ------------------------------------------------------------
# Problem 11:
# Create a function filter_even that:
# - takes a list of integers
# - returns a new list containing only even numbers
# ------------------------------------------------------------

# Write your code below

def filter_even(integers):
    new_list = []
    for n in integers:
        if n % 2 == 0:
            new_list.append(n)
    return new_list

# ------------------------------------------------------------
# Problem 12:
# Create a function factorial using recursion:
# - input: n
# - output: factorial of n
# ------------------------------------------------------------

# Write your code below

def factorial(n): 
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)

# ------------------------------------------------------------
# Problem 13:
# Create a function swap_numbers that:
# - takes two numbers a and b
# - returns them swapped
# ------------------------------------------------------------

# Write your code below

def swap_numbers(a, b):
    return (b , a)

# ------------------------------------------------------------
# Problem 14:
# Write a lambda function triple that:
# - input: a number
# - output: number * 3
# ------------------------------------------------------------

# Write your code below

triple = lambda number: number * 3

# 15. Write a function `square(n)` that returns the square of a number.

def square(n):
    return n ** 2

# 16. Write a function `is_even(n)` that returns True if n is even, else False.

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# 17. Write a function `max_of_two(a, b)` that returns the larger number.

def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b

# 18. Write a function `reverse_string(s)` without using slicing.

def reverse_string(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev

# 19. Write a recursive function `sum_upto(n)` that returns 1 + 2 + ... + n.

def sum_upto_(n):
     if n == 0:
         return n
     else:
         return n + sum_upto_(n - 1)

# 20. Write a recursive function `power(base, exp)` that calculates base^exp.

def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)

# 21. Write a function that swaps three numbers (a → b → c → a).

def swap(a, b, c):
    return b, c, a

# 22. Write a lambda function `last_digit` that returns the last digit of a number.

last_digit = lambda n: n % 10

# 23. Write a function `count_vowels(s)` that returns the number of vowels in a string.

def count_vowel(s):
    vowel = 0
    s = s.lower()
    for char in s:
        if char in "aeiou":
            vowel += 1
    return vowel

# 24. Write a function `merge_lists(l1, l2)` that returns a single combined list.

def merge_lists(l1, l2):
    return l1 + l2

# 25. Write a function `is_palindrome(s)` that checks if a string is palindrome.

def is_palindrome_(s):
    reverse = ""
    for a in s:
        reverse = a + reverse
    if reverse == s:
        return True
    else:
        return False

# 26. Write a function `min_of_three(a, b, c)` without using min().

def min_of_three(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <=c:
        return b
    else:
        return c

# 27. Write a function `factorial_iterative(n)` using loop (not recursion).

def factorial_iterative(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# 28. Write a function `unique_elements(lst)` that returns list of unique elements.

def unique_elements(lst):
    unique_set = set(lst)
    unique_list = list(unique_set)
    return unique_list

# 29. Write a function `multiply_list(lst)` that multiplies all numbers in a list.

def multiply_list(lst):
    mul = 1
    for s in lst:
        mul *= s
    return mul

# 30. Write a function `safe_divide(a, b)` that returns "Error" if b == 0 else a/b.

def safe_divide_(a, b):
    if b == 0:
        return "Error"
    else:
        return a / b

# 31. Write a function `second_largest(lst)` that:
# - takes a list of integers
# - returns the second largest number
# - assume list has at least 2 unique numbers
# - use only basic Python syntax (max(), remove(), copy(), etc.)

def second_largest(lst):
    temp = lst.copy()
    temp.remove(max(temp))
    second_lar = max(temp)
    return second_lar

# 32. Write a function `count_occurrences(lst, x)` that:
# - takes a list `lst` and a value `x`
# - returns the number of times `x` appears in the list

def count_occurence(lst, x):
    count = 0
    for a in lst:
        if x == a:
            count += 1
    return count

# 33. Write a function `remove_duplicates(lst)` that:
# - takes a list
# - returns a new list with duplicates removed
# - order does not matter

def remove_duplicates(lst):
    lst_set = set(lst)
    lst_unique = list(lst_set)
    return lst_unique

# 34. Write a function `flatten_list(lst_of_lsts)` that returns a single flattened list from a list of lists.

def flatten_list(lst_of_lsts):
    flat = []
    for sublists in lst_of_lsts:
        for item in sublists:
            flat.append(item)
    return flat

# 35. Write a function `greet_all(names)` that takes a list of names and prints "Hello, <name>!" for each.

def greet_all(names):
    for name in names:
        print(f"Hello, {name}!")

# 36. Write a function `is_prime(n)` that returns True if n is prime, else False.

def is_prime(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return True
            

# 37. Write a function `sum_digits(n)` that returns the sum of digits of a number.

def sum_digits(n):
    sum_ = 0
    n_list =  list(str(n))
    for x in n_list:
        x = int(x)
        sum_ += x
    return sum_

# 38. Write a function `reverse_words(sentence)` that takes a string and returns the string with words reversed (word order, not letters).

def reverse_words(sentence):
    words = sentence.split()
    words_rev = ""
    for x in words:
        words_rev = x + " " + words_rev
    return words_rev

reverse_words("hey bro how are uh")

# 39. Write a lambda function `quadruple` that multiplies its input by 4.

quadruple = lambda x: x * 4

# 40. Write a function `factorial_recursive(n)` that returns the factorial of n using recursion.

def factorial_recursive_(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive_(n -1)
    
# 41. Write a function `find_max_length(words)` that:
# - takes a list of strings
# - returns the length of the longest string
# - use loops only (no max())

def find_max_length(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return len(longest)

# 42. Write a function `count_vowels(s)` that:
# - takes a string
# - returns the number of vowels

def count_vowels(s):
    count = 0
    s = s.lower()
    for x in s:
        if x in "aeiou":
            count += 1
    return count

# 43. Write a function `merge_dicts(d1, d2)` that:
# - takes two dictionaries
# - returns a new dictionary containing all key:value pairs
# - if a key is in both, keep the value from d2

def merge_dicts(d1, d2):
    merged = {}
    for key in d1:
        merged[key] = d1[key]
    for key in d2:
        merged[key] = d2[key]
    return merged


# 44. Write a function `multiply_numbers(*args)` that:
# - takes any number of numeric arguments
# - returns their product

def multiply_numbers(*s):
    product = 1
    for a in s:
        product *= a
    return product

# 45. Write a function `print_profile(**kwargs)` that:
# - prints all key:value pairs passed as keyword arguments

def print_profile(**kwarg):
    for key, value in kwarg.items():
        print(key, ":", value)

# 46. Write a function `reverse_list(lst)` that:
# - returns a new list with elements in reverse order
# - use loops only (no slicing)

def reverse_list(lst):
    rev_lst = []
    for x in lst:
        rev_lst.insert(0, x)
    return rev_lst

# 47. Write a function `is_palindrome(s)` that:
# - returns True if the string is a palindrome, else False
# - use loops only (no slicing)

def is_palindrome(s):
    rev_s = ""
    for a in s:
        rev_s = a + rev_s
    if rev_s == s:
        return True
    else:
        return False
        
# 48. Write a lambda function `cube` that:
# - returns the cube of its input

cube = lambda x: x * x * x

# 49. Write a function `sum_upto(n)` that:
# - returns 1 + 2 + ... + n

def sum_upto(n):
    sum_ = 0
    for x in range(1, n + 1):
        sum_ += x
    return sum_

# 50. Write a function `safe_divide(a, b)` that:
# - returns "Error" if b == 0 else a/b

def safe_divide(a, b):
    if b == 0:
        return "Error"
    else:
        return a / b
    
# 51. merge_two_dicts(d1, d2)
# - takes two dictionaries
# - returns a new dictionary combining all key:value pairs
# - no need to handle duplicates specially

def merge_two_dicts_(d1, d2):
    combine = {}
    for key in d1:
        combine[key] = d1[key]
    for key in d2:
        combine[key] = d2[key]
    return combine

# 52. is_palindrome_simple(s)
# - takes a string
# - returns True if string is the same forwards and backwards, else False
# - just use loops to compare characters

def is_palindrome_simple(s):
    rev_s = ""
    for a in s:
        rev_s = a + rev_s
    if s == rev_s:
        return True
    else:
        return False

# 53. print_all_details(**kwargs)
# - prints all key:value pairs using **kwargs
# - format: key: value

def print_all_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

# 54. reverse_string_loop_simple(s)
# - reverses a string using loops only
# - return the reversed string

def reverse_string_loop_simple(s):
    rev_s = ""
    for a in s:
        rev_s = a + rev_s
    return rev_s

# 55. sum_upto_simple(n)
# - takes a number n
# - returns sum of numbers from 1 to n using a loop (no recursion)
# - just practice loops + return

def sum_upto_simple(n):
    sum = 0
    for a in range(1, n + 1):
        sum += a
    return sum

# 56. create_greeting(name)
# - takes a name
# - returns "Hello, <name>!"
def create_greeting(name):
    do = f"Hello, {name}!"
    return do

# 57. add_numbers(a, b, c=0)
# - takes 2 required numbers and 1 optional (default=0)
# - returns their sum
def add_numbers(a, b, c=0):
    _sum_ = a + b + c
    return _sum_

# 58. multiply_all(*args)
# - takes any number of numbers
# - returns their product
def multiply_all(*args):
    product = 1
    for n in args:
        product *= n
    return product

# 59. print_user_info(**kwargs)
# - prints all key:value pairs passed as keyword arguments
def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

# 60. factorial_loop(n)
# - returns factorial of n using a loop
def factorial_loop(n):
    factorial = 1
    for j in range(1, n + 1):
        factorial *= j
    return factorial

# 61. factorial_recursive(n)
# - returns factorial of n using recursion
def factorial_recursive(n):
    if n == 0:  
        return 1
    else:
        return n * factorial_recursive(n - 1)

# 62. reverse_string_loop(s)
# - reverses a string using a loop (no slicing)
def reverse_string_loop(s):
    rev_s = ""
    for a in s:
        rev_s = a + rev_s
    return rev_s

# 63. count_vowels_in_string(s)
# - returns the number of vowels in the string
def count_vowels_in_string(s):
    count = 0
    s = s.lower()
    for a in s:
        if a in "aeiou":
            count += 1
    return count

# 64. merge_two_dicts(d1, d2)
# - returns a new dictionary combining d1 and d2
# - if keys overlap, keep value from d2
def merge_two_dicts(d1, d2):
    combine = {}
    for key, value in d1.items():
        combine[key] = d1[key]
    for key, value in d2.items():
        combine[key] = d2[key]
    return combine

# 65. sum_upto_n(n)
# - returns sum of 1+2+...+n using a loop
# - then also write a recursive version
def sum_upto_n(n):
    sum__ = 0
    for s in range(1, n + 1):
        sum__ += s
    return sum__

def sum_upto_n_recursive(n):
    if n == 0:
        return 0
    else:
        return n + sum_upto_n_recursive(n - 1)

# ------------------------------------------------------------
# 66. Write a function `count_consonants(s)` that:
# - takes a string `s`
# - returns the number of consonants
# - ignore spaces
# - count only alphabet characters
# ------------------------------------------------------------

def count_consonants(s):
    consonant = 0
    for char in s:
        if char.lower() not in "aeiou" and char.isalpha():
            consonant += 1
    return consonant

# ------------------------------------------------------------
# 67. Write a function `rotate_list_left(lst, k)` that:
# - takes a list `lst` and an integer `k`
# - rotates the list to the left by `k` positions
# - return the rotated list
# Example:
# rotate_list_left([1,2,3,4,5], 2) → [3,4,5,1,2]
# ------------------------------------------------------------

def rotate_list_left(lst, k):
    if len(lst) == 0:
        return lst

    k = k % len(lst)
    rotated = []

    for i in range(k, len(lst)):
        rotated.append(lst[i])

    for i in range(k):
        rotated.append(lst[i])

    return rotated

# ------------------------------------------------------------
# 68. Write a recursive function `count_digits(n)` that:
# - takes an integer `n`
# - returns the number of digits in `n`
# - do NOT convert the number to string
# ------------------------------------------------------------

def count_digits(n):
    if n < 0:
        n = -n

    if n < 10:
        return 1

    return 1 + count_digits(n // 10)
