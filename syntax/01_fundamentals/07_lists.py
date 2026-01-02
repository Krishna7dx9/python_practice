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
last_item = nums.pop()
nums.sort()
nums.reverse()
count_once = nums.count(1)
index_of_4 = nums.index(4) if 4 in nums else None
nums.clear()

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
mid = (low + high) // 2
print(mid)
print(numbers_p1[mid])

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
even_c = []

for n in nums_p3:
    if n % 2 == 0:
        print(n)
        even_c.append(n)
print(len(even_c))

# ------------------------------------------------------------
# Problem 4:
# Given a list:
# - Sort it
# - Reverse it
# - Print both results
# ------------------------------------------------------------

arr_p4 = [9, 2, 14, 1, 5, 8]
# Your solution here

arr_p4.sort()
print(arr_p4)

arr_p4.reverse()
print(arr_p4)

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

num_0 = list(map(int, input("Enter numbers: ").split()))
maxi = max(num_0)
mini = min(num_0)
summ = sum(num_0)

print(f"Maximum: {maxi}")
print(f"Minimum: {mini}")
print(f"Sum: {summ}")

# ------------------------------------------------------------
# Problem 6:
# Create a list of 5 numbers.
# Make a NEW list with each number squared using list comprehension.
# ------------------------------------------------------------

list_p6 = [2, 4, 6, 8, 10]
print(list_p6)
# Your solution here

squared_list_p6 = [n * n for n in list_p6]
print(squared_list_p6)

# ------------------------------------------------------------
# Problem 7:
# Remove duplicates from a list WITHOUT using set().
# (Use a loop and construct a new list)
# ------------------------------------------------------------

list_with_dupes_p7 = [1, 3, 3, 5, 1, 7, 7, 2]
# Your solution here

new_list = []
for n in list_with_dupes_p7:
    if n not in new_list:
        new_list.append(n)

# ------------------------------------------------------------
# Problem 8:
# Given a list of numbers, copy it CORRECTLY (not reference copy).
# Then modify the new list and print BOTH lists.
# ------------------------------------------------------------

orig_list_p8 = [10, 20, 30]
# Your solution here

orig_list_p8_copy = orig_list_p8[:]
orig_list_p8_copy.append(5)

print(orig_list_p8_copy)
print(orig_list_p8)

# ------------------------------------------------------------
# Problem 9:
# Given a list of numbers, find the second largest number without using max() twice.
# ------------------------------------------------------------

def second_largest_number(lst):
    lst_copy = lst.copy()
    max_1 = max(lst_copy)
    lst_copy.remove(max_1)
    if len(lst_copy) >= 1:
        max_2 = lst_copy[0]
        for n in lst_copy:
            if n > max_2:
                max_2 = n
        return max_2

# ------------------------------------------------------------
# Problem 10:
# Count how many times a specific value occurs in a list.
# Input: list and value
# ------------------------------------------------------------

def count_occurrences(lst, val):
    lst_count = lst.count(val)
    return lst_count

# ------------------------------------------------------------
# Problem 11:
# Merge two lists into a new list.
# ------------------------------------------------------------

def merge_lists(l1, l2):
     l3 = l1 + l2
     return l3

# ------------------------------------------------------------
# Problem 12:
# Find all indices of a value in a list.
# Input: list and value
# Output: list of indices
# ------------------------------------------------------------

def find_all_indices(lst, val):
    indices = []
    for  i, n in enumerate(lst):
        if n == val:
            indices.append(i)
    return indices

# ------------------------------------------------------------
# Problem 13:
# Reverse a list using a loop (no slicing, no reverse()).
# ------------------------------------------------------------

def reverse_list_loop(lst):
    rev_lst = []
    for i in lst:
        rev_lst = [i] + rev_lst
    return rev_lst

# ------------------------------------------------------------
# Problem 14:
# Create a list of squares from 1 to n using list comprehension.
# ------------------------------------------------------------

def squares_list(n):
    squares = [x * x for x in range(1, n + 1)]
    return squares

# ------------------------------------------------------------
# Problem 15:
# Remove all duplicates from a list without using set().
# ------------------------------------------------------------

def remove_duplicates_loop(lst):
    new_lst = []
    for n in lst:
        if n not in new_lst:
            new_lst.append(n)
    return new_lst

# ------------------------------------------------------------
# Problem 16:
# Check if a list is a palindrome (same forwards and backwards).
# ------------------------------------------------------------

def is_list_palindrome(lst):
    lst_rev = lst[:]
    lst_rev.reverse()
    if lst == lst_rev:
        return True
    else:
        return False

# ------------------------------------------------------------
# Problem 17:
# Given a list of numbers, return a new list with only even numbers.
# ------------------------------------------------------------

def filter_even_numbers(lst):
    even_num = []
    for n in lst:
        if n % 2 == 0:
            even_num.append(n)
    return even_num


# ------------------------------------------------------------
# Problem 18:
# Given a nested list (list of lists), flatten it into a single list.
# ------------------------------------------------------------

def flatten_nested_list(lst_of_lsts):
    flatten_lst = []
    for sublist in lst_of_lsts:
        for element in sublist:
            flatten_lst.append(element)
    return flatten_lst

# ------------------------------------------------------------
# Problem 19:
# Count the total number of elements in a nested list.
# Example: [[1,2], [3,4,5]] → 5
# ------------------------------------------------------------

def count_total_elements(lst_of_lsts):
    count = 0
    for sublist in lst_of_lsts:
        for element in sublist:
            count += 1
    return count

# ------------------------------------------------------------
# Problem 20:
# Given a list, return a new list with elements multiplied by their index.
# ------------------------------------------------------------

def multiply_by_index(lst):
    element_x_index = []
    for i, x in enumerate(lst):
        multi = i * x
        element_x_index.append(multi)
    return element_x_index

