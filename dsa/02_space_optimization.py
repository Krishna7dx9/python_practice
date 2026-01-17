# ============================================================
# DSA — SPACE COMPLEXITY (COMPLETE NOTES)
# Purpose:
#   - Interview-ready reference
#   - For GitHub / practice folder
#   - Analysis-only (do NOT run)
# ============================================================


# ------------------------------------------------------------
# 1. What is Space Complexity?
# ------------------------------------------------------------
# Space Complexity measures the EXTRA memory used by an algorithm
# as the input size grows.
#
# We count:
#   - Variables
#   - Data structures (list, dict, set, etc.)
#   - Recursive call stack
#
# We do NOT count:
#   - Input itself
#   - Output (unless explicitly mentioned)
#
# Formula:
#   Total Space = Auxiliary Space + Call Stack Space
# ------------------------------------------------------------


# ------------------------------------------------------------
# 2. Auxiliary Space
# ------------------------------------------------------------
# Auxiliary Space = Memory YOU explicitly create.
#
# Includes:
#   - Variables
#   - Temporary lists / dicts / sets
#   - Arrays created by slicing
#
# Examples:
#
# a = 10            -> O(1)
# temp = []         -> O(n) if it grows with input
# mp = {}           -> O(n) if it stores n elements
# ------------------------------------------------------------


# ------------------------------------------------------------
# 3. Call Stack Space
# ------------------------------------------------------------
# Call Stack Space = Memory used by recursive function calls.
#
# Each recursive call stores:
#   - Parameters
#   - Local variables
#   - Return address
#
# Rules:
#   - Iterative code  -> O(1) stack
#   - Recursive code -> Depends on recursion depth
# ------------------------------------------------------------


# ------------------------------------------------------------
# 4. Constant Space — O(1)
# ------------------------------------------------------------
def constant_space_example(arr):
    total = 0
    for x in arr:
        total += x
    return total

# Auxiliary Space: O(1)
# Call Stack Space: O(1)
# Total Space: O(1)
#
# Note:
#   - Loop does NOT increase space
# ------------------------------------------------------------


# ------------------------------------------------------------
# 5. Linear Auxiliary Space — O(n)
# ------------------------------------------------------------
def linear_space_example(arr):
    res = []
    for x in arr:
        res.append(x)
    return res

# Auxiliary Space: O(n)  (extra list grows with input)
# Call Stack Space: O(1)
# Total Space: O(n)
# ------------------------------------------------------------


# ------------------------------------------------------------
# 6. Linear Recursion Stack — O(n)
# ------------------------------------------------------------
def linear_recursion(n):
    if n == 0:
        return
    linear_recursion(n - 1)

# Auxiliary Space: O(1)
# Call Stack Space: O(n)
# Total Space: O(n)
#
# Reason:
#   One recursive call per element
# ------------------------------------------------------------


# ------------------------------------------------------------
# 7. Divide & Conquer Recursion Stack — O(log n)
# ------------------------------------------------------------
def divide_and_conquer(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = divide_and_conquer(arr[:mid])
    right = divide_and_conquer(arr[mid:])
    return left + right

# Auxiliary Space: O(n)
#   - Slicing creates new arrays
#   - Merging creates new array
#
# Call Stack Space: O(log n)
#   - Input size halves each call
#
# Total Space: O(n)
# ------------------------------------------------------------


# ------------------------------------------------------------
# 8. Slicing Rule (VERY IMPORTANT)
# ------------------------------------------------------------
# Any slicing operation creates a NEW array:
#
# arr[1:]
# arr[:mid]
# arr[mid:]
#
# Therefore:
#   Auxiliary Space = O(n)
#
# Even if used inside recursion.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 9. In-Place Algorithms — O(1) Space
# ------------------------------------------------------------
def reverse_array_in_place(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

# Auxiliary Space: O(1)
# Call Stack Space: O(1)
# Total Space: O(1)
#
# In-place = No extra data structures
# ------------------------------------------------------------


# ------------------------------------------------------------
# 10. Sorting Algorithms — Space Summary
# ------------------------------------------------------------
# Bubble Sort     -> O(1)
# Selection Sort  -> O(1)
# Insertion Sort  -> O(1)
# Merge Sort      -> O(n)
# Quick Sort      -> O(log n) stack (average)
# ------------------------------------------------------------


# ------------------------------------------------------------
# 11. One-Line Interview Rules (Memorize)
# ------------------------------------------------------------
# - Variables ≠ growing space
# - Loops ≠ space
# - Recursion always costs stack space
# - Slicing always costs auxiliary space
# - n → n-1 recursion → O(n) stack
# - n → n/2 recursion → O(log n) stack
# ------------------------------------------------------------


# ------------------------------------------------------------
# 12. Final Summary
# ------------------------------------------------------------
# Space Complexity = Auxiliary Space + Call Stack Space
#
# Always mention BOTH in interviews.
# ------------------------------------------------------------


# Q1
# What is the space complexity of this function and WHY?

def f1(arr):
    s = 0
    for x in arr:
        s += x
    return s

# Space: O(1) — only constant variables used

# Q2
# What is the space complexity?

def f2(arr):
    res = []
    for x in arr:
        if x % 2 == 0:
            res.append(x)
    return res

# Space: O(n) — extra list res can store up to n elements

# Q3
# What is the space complexity (include recursion stack)?

def f3(n):
    if n == 0:
        return
    f3(n - 1)

# Auxiliary Space - O(1)
# Call Stack Space - O(n)
# Total space - O(n)

# Q4
# What is the space complexity and why?

def f4(arr):
    if not arr:
        return
    f4(arr[1:])

# Auxiliary Space - O(n)         -- (due to slicing, creates a NEW array every call)
# Call Stack Space - O(n)        -- (recursion depth)
# Total space - O(n)

# Q5
# Binary search written iteratively.
# What is the space complexity?

def f5(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return -1

# Auxiliary Space: O(1)
# Call Stack Space: O(1)
# Total Space: O(1)

# ============================================================
# SPACE COMPLEXITY — RETEST (ANALYSIS ONLY)
# ============================================================
# For EACH function below, state:
# 1) Auxiliary Space
# 2) Call Stack Space
# 3) Total Space
#
# One line per function. No extra explanation.
# ============================================================


def func_a(arr):
    if not arr:
        return
    func_a(arr[1:])

# 1) Auxiliary Space    -- O(n)
# 2) Call Stack Space   -- O(n)
# 3) Total Space        -- O(n)

# slicing creates new array every call, Every recursive call adds ONE frame to the call stack

def func_b(arr, i):
    if i == len(arr):
        return
    func_b(arr, i + 1)

# 1) Auxiliary Space     -- O(1)
# 2) Call Stack Space    -- O(n)
# 3) Total Space         -- O(n)

# No extra space, recursion depth grows

def func_c(arr):
    i = 0
    while i < len(arr):
        print(arr[i])
        i += 1

# 1) Auxiliary Space     -- O(1)
# 2) Call Stack Space    -- O(1)
# 3) Total Space         -- O(1)

# No extra space i is constant, no call stack

def func_d(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

# 1) Auxiliary Space     -- O(1)
# 2) Call Stack Space    -- O(1)
# 3) Total Space         -- O(1)

# left, right are constant No extra space, no call stack

def func_e(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = func_e(arr[:mid])
    right = func_e(arr[mid:])
    return left + right

# 1) Auxiliary Space     -- O(n) (due to slicing + merge arrays)
# 2) Call Stack Space    -- O(logn) (divide and conquer)
# 3) Total Space         -- O(logn)

# slicing created new array every call, no call stack