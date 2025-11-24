# ------------------------------------------------------------
# 1. Creating Lists
# ------------------------------------------------------------

# empty list
empty_list = []

# list of numbers
numbers = [10, 20, 30, 40, 50]

# list of strings
fruits = ["apple", "banana", "mango"]

# mixed list (not recommeded in DSA but allowed in python)
mixed_list = ["Kris", 25, True, 45.63]

# ------------------------------------------------------------
# 2. Accessing Elements (Indexing)
# ------------------------------------------------------------

# indexing starts from 0
first_fruit = fruits[0]        # "apple"
second_numbers = numbers[1]    # 20

# negative indexing (from end)
last_fruit = fruits[-1]
second_last_number = numbers[-2]

# ------------------------------------------------------------
# 3. Slicing Lists
# ------------------------------------------------------------

# list[start:end]     end index NOT included
slice_demo = numbers[1:3]

# list[start:end:step]
step_slice = numbers[0:4:2]

# full copy using slicing 
full_copy = numbers[:]

# ------------------------------------------------------------
# 4. Updating Values
# ------------------------------------------------------------

numbers[0] = 99
fruits[1] = "orange"

# ------------------------------------------------------------
# 5. List Methods (VERY Important)
# ------------------------------------------------------------

nums = [3, 4, 1]

nums.append(5)
nums.insert(1, 10)
nums.remove(10)
last_item = nums.pop
nums.sort()
nums.reverse()
count_once = nums.count(1)
index_of_4 = nums.index(4) if 4 in nums else None
nums.clear

# ------------------------------------------------------------
# 6. Looping Through Lists
# ------------------------------------------------------------

loop_list = [4, 8, 12]

# for loop
for x in loop_list:
    print(x)

# while loop
i = 0
while i < len(loop_list):
    print(loop_list[i])
    i += 1

# ------------------------------------------------------------
# 7. Copying Lists (VERY IMPORTANT)
# ------------------------------------------------------------

list_a = [1, 2, 2]
list_b = list_a                              # wrong (same memory reference)
list_c = list_a.copy()                       # creates correct copy
list_d = list_a[:]                           # also correct

# ------------------------------------------------------------
# 8. List Comprehension
# ------------------------------------------------------------

squares = [n*n for n in range(10)]
even_nums = [n for n in range(20) if n % 2 == 0]

# ------------------------------------------------------------
# PRACTICE PROBLEMS — LISTS
# ------------------------------------------------------------


# ------------------------------------------------------------
# Problem 1:
# Create a list of 7 numbers.
# Print:
# - first element
# - last element
# - middle element
# ------------------------------------------------------------

numbers_p1 = [5, 12, 3, 19, 8, 1, 7]
# Your solution here

print(numbers_p1[0])
print(numbers_p1[-1])
low = 0
high = len(numbers_p1)
mid = (low + high) / 2
print(mid)
# print(numbers_p1[mid])

# ------------------------------------------------------------
# Problem 2:
# Given a list of strings, change the 2nd and last value.
# ------------------------------------------------------------

names_p2 = ["kris", "kabir", "arjun", "maya"]
# Your solution here

names_p2[1] = "Kabir"
names_p2[-1] = "Maya"

# ------------------------------------------------------------
# Problem 3:
# From a list of numbers:
# - Print only even numbers
# - Print their count
# ------------------------------------------------------------

nums_p3 = [4, 11, 22, 9, 16, 7, 30]
# Your solution here

n = 0
while n < len(nums_p3):
    if nums_p3[n] % 2 == 0:
       print(nums_p3[n])
    n += 1
else:
    n += 1



# ------------------------------------------------------------
# Problem 4:
# Given a list:
# - Sort it
# - Reverse it
# - Print both results
# ------------------------------------------------------------

arr_p4 = [9, 2, 14, 1, 5, 8]
# Your solution here



# ------------------------------------------------------------
# Problem 5:
# Input: numbers in one line → convert to list of ints.
# Then print:
# - max
# - min
# - sum
# ------------------------------------------------------------

# Example input: 5 10 2 8
# Your solution here



# ------------------------------------------------------------
# Problem 6:
# Create a list of 5 numbers.
# Make a NEW list with each number squared using list comprehension.
# ------------------------------------------------------------

list_p6 = [2, 4, 6, 8, 10]
# Your solution here



# ------------------------------------------------------------
# Problem 7:
# Remove duplicates from a list WITHOUT using set().
# (Use a loop and construct a new list)
# ------------------------------------------------------------

list_with_dupes_p7 = [1, 3, 3, 5, 1, 7, 7, 2]
# Your solution here



# ------------------------------------------------------------
# Problem 8:
# Given a list of numbers, copy it CORRECTLY (not reference copy).
# Then modify the new list and print BOTH lists.
# ------------------------------------------------------------

orig_list_p8 = [10, 20, 30]
# Your solution here
