# ============================================================
# PYTHON ARRAYS (LISTS) — COMPLETE DSA-READY NOTES
# ONE CODE FILE — NO FLUFF
# ============================================================

# ------------------------------------------------------------
# 1. WHAT "ARRAY" MEANS IN PYTHON
# ------------------------------------------------------------
# Python does NOT have a built-in low-level array like C/C++.
# For DSA and interviews:
#   ARRAY = PYTHON LIST (dynamic array)
#
# The `array` module exists but is rarely used in interviews.

# ------------------------------------------------------------
# 2. CREATING ARRAYS (LISTS)
# ------------------------------------------------------------
arr1 = []                  # empty array
arr2 = [1, 2, 3, 4]        # integers
arr3 = list()              # constructor

# DSA RULE:
# Logically keep same-type elements even though Python allows mixed types.

# ------------------------------------------------------------
# 3. INDEXING (0-BASED)
# ------------------------------------------------------------
arr = [10, 20, 30, 40]

first = arr[0]     # 10
last = arr[-1]     # 40
second_last = arr[-2]  # 30

# Accessing invalid index → IndexError
# arr[10]

# Time Complexity:
# Index access → O(1)

# ------------------------------------------------------------
# 4. UPDATING ELEMENTS
# ------------------------------------------------------------
arr[1] = 99        # [10, 99, 30, 40]

# Time Complexity:
# Update by index → O(1)

# ------------------------------------------------------------
# 5. LENGTH OF ARRAY
# ------------------------------------------------------------
n = len(arr)

# Time Complexity:
# len(arr) → O(1)

# ------------------------------------------------------------
# 6. TRAVERSING AN ARRAY (VERY IMPORTANT)
# ------------------------------------------------------------

# Index-based traversal (PREFERRED FOR DSA)
for i in range(len(arr)):
    print(arr[i])

# Element-based traversal (READ-ONLY LOGIC)
for x in arr:
    print(x)

# Time Complexity:
# Traversal → O(n)

# ------------------------------------------------------------
# 7. ADDING ELEMENTS
# ------------------------------------------------------------

# Append at end
arr.append(50)

# Time Complexity:
# append → Amortized O(1)

# Insert at specific index
arr.insert(0, 5)

# Time Complexity:
# insert → O(n) (shifting elements)

# ------------------------------------------------------------
# 8. REMOVING ELEMENTS
# ------------------------------------------------------------

# Remove last element
arr.pop()          # O(1)

# Remove element at index
arr.pop(0)         # O(n)

# Remove by value (first occurrence)
arr.remove(30)     # O(n)

# ------------------------------------------------------------
# 9. SEARCHING IN ARRAY
# ------------------------------------------------------------

# Membership check
exists = 20 in arr

# Time Complexity:
# Linear search → O(n)

# DSA RULE:
# Assume built-ins are NOT allowed unless stated.

# ------------------------------------------------------------
# 10. SLICING (CREATES NEW ARRAY)
# ------------------------------------------------------------
arr = [1, 2, 3, 4, 5]
sub = arr[1:4]     # [2, 3, 4]

# Time Complexity:
# O(k), where k = slice length
# Space Complexity:
# O(k) (new array created)

# ------------------------------------------------------------
# 11. IMPORTANT DSA TRUTHS (MEMORIZE)
# ------------------------------------------------------------
# - Arrays are contiguous in concept
# - Random access is fast → O(1)
# - Insert/Delete in middle is slow → O(n)
# - Most problems require full traversal → O(n)

# ============================================================
# PYTHON ARRAYS — TEST 1
# ============================================================

# Q1
# Create an array of the first 5 natural numbers.
# Then update the 3rd element to 100.

nums = [1, 2, 3, 4, 5]
nums[2] = 100

# Q2
# Given arr = [10, 20, 30, 40, 50]
# Print all elements using an INDEX-based loop only.

arr = [10, 20, 30, 40, 50]

for x in range(len(arr)):
    print(arr[x])

# Q3
# Write a function that returns the last element of an array.
# If the array is empty, return None.

def last(arr):
    if not arr:
        return None
    else:
        return arr[-1]

hey = last(arr)
print(hey)

# Q4
# Write a function that counts how many times a given target
# appears in an array WITHOUT using count().

def counts(arr, target):
    count = 0
    for x in arr:
        if x == target:
            count += 1
    return count

lets_count = counts(arr, 2)
print(lets_count)

# Q5
# Given arr = [1, 2, 3, 4, 5]
# Remove the element at index 2.
# Print the array after removal.

arr = [1, 2, 3, 4, 5]

arr.pop(2)
print(arr)

# Q6
# What is the time complexity of:
# (a) arr.append(x)
# (b) arr.insert(0, x)
# (c) accessing arr[i]
# Write answers as comments.

# (a) Amortized - O(1)
# (b) O(n)
# (c) O(1)

# Q7
# Write a function that checks whether an array is empty
# WITHOUT using len().

def check_empty(arr):
    return not arr

# ====================================================
# PYTHON ARRAYS — TEST 2 (STRICT)
# ====================================================

# Q1
# Write a function that returns the first element of an array.
# If the array is empty, return None.

def first_element(arr):
    if not arr:
        return None
    else:
        return arr[0]

# Q2
# Write a function that returns True if an array is empty,
# False otherwise. Do NOT use len().

def empty_check(arr):
    return not arr

# Q3
# Write a function that counts occurrences of a target element
# using INDEX-based traversal only.

def count_occurence(arr, target):
    count = 0
    for x in range(len(arr)):
        if arr[x] == target:
            count += 1
    return count

# Q4
# Given arr = [5, 10, 15, 20]
# Replace every element at an EVEN index with 0.
# Print the final array.

arr = [5, 10, 15, 20]

for x in range(len(arr)):
    if x % 2 == 0:
        arr[x] = 0

print(arr)

# Q5
# Write the time complexity as comments:
# (a) Traversing an array
# (b) Removing element at index 0
# (c) append() on Python list

# (a) O(n)
# (b) O(n)
# (c) Amortised - O(1)