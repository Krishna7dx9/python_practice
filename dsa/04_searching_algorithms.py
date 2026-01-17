# ============================================================
# SEARCHING ALGORITHMS — COMPLETE NOTES (DSA READY)
# ============================================================
# Goal:
# Find the position / existence / count of a target element
# in a data structure.
#
# Core Interview Focus:
# - Correct algorithm choice
# - Edge cases
# - Time & Space Complexity
# ============================================================


# ============================================================
# 1. LINEAR SEARCH (SEQUENTIAL SEARCH)
# ============================================================
# Definition:
# Traverse elements one by one until the target is found
# or the list ends.
#
# Works on:
# - Sorted data
# - Unsorted data
#
# Use when:
# - Data is unsorted
# - Dataset is small
# - One-pass constraint exists
#
# Do NOT use when:
# - Data is large and sorted (Binary Search is better)
# ------------------------------------------------------------

def linear_search_first(arr, target):
    """
    Returns index of FIRST occurrence of target, else -1
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def linear_search_last(arr, target):
    """
    Returns index of LAST occurrence of target, else -1
    """
    last = -1
    for i in range(len(arr)):
        if arr[i] == target:
            last = i
    return last


def linear_search_count(arr, target):
    """
    Counts number of occurrences of target
    """
    count = 0
    for x in arr:
        if x == target:
            count += 1
    return count


def linear_search_exists(arr, target):
    """
    Returns True if target exists, else False
    """
    for x in arr:
        if x == target:
            return True
    return False


# Time Complexity:
# Best Case    : O(1)
# Average Case : O(n)
# Worst Case   : O(n)
#
# Space Complexity:
# O(1)
#
# Notes:
# - `x in list` is O(n)
# - list.index(x) is O(n) and raises error if not found
# - Never use Binary Search on unsorted data


# ============================================================
# 2. BINARY SEARCH
# ============================================================
# Definition:
# Repeatedly divide the search space in half.
#
# PRECONDITION:
# Data MUST be sorted.
#
# Use when:
# - Data is sorted
# - Fast lookup is required
#
# Do NOT use when:
# - Data is unsorted
# - Frequent insertions/deletions without re-sorting
# ------------------------------------------------------------

def binary_search(arr, target):
    """
    Standard Binary Search
    Returns index of target, else -1
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Time Complexity:
# Best Case    : O(1)
# Average Case : O(log n)
# Worst Case   : O(log n)
#
# Space Complexity:
# Iterative : O(1)
# Recursive : O(log n) (call stack)


# ============================================================
# 3. BINARY SEARCH VARIANTS (INTERVIEW CRITICAL)
# ============================================================

def binary_search_first(arr, target):
    """
    Finds FIRST occurrence of target in sorted array
    """
    left, right = 0, len(arr) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            ans = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return ans


def binary_search_last(arr, target):
    """
    Finds LAST occurrence of target in sorted array
    """
    left, right = 0, len(arr) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            ans = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return ans


# Time Complexity:
# O(log n)
#
# Space Complexity:
# O(1)


# ============================================================
# 4. COMPARISON SUMMARY (INTERVIEW FAVORITE)
# ============================================================
# Linear Search:
# - Works on unsorted data
# - O(n)
# - Simple, slow for large input
#
# Binary Search:
# - Requires sorted data
# - O(log n)
# - Fast, but precondition matters
#
# Interview Rule:
# If data is sorted → THINK BINARY SEARCH FIRST


# ============================================================
# 5. EDGE CASES YOU MUST HANDLE
# ============================================================
# - Empty list
# - Single element
# - Target not present
# - Duplicate elements
#
# Expected behavior:
# - Index-based searches → return -1 if not found
# - Count → return 0
# - Exists → return False


# ============================================================
# END OF SEARCHING ALGORITHMS NOTES
# ============================================================
