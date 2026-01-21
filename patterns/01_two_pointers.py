# ============================================================
# ARRAY PROBLEM PATTERNS — TWO POINTERS
# ONE CODE FILE (DSA / INTERVIEW READY)
# ============================================================

# ------------------------------------------------------------
# WHAT IS TWO POINTERS
# ------------------------------------------------------------
# Two pointers is a technique where two indices traverse
# an array in a controlled way to solve problems efficiently,
# often reducing time complexity from O(n^2) to O(n).

# ------------------------------------------------------------
# WHEN TO USE TWO POINTERS
# ------------------------------------------------------------
# - Array is SORTED
# - Need to find pairs
# - Reverse / palindrome checks
# - In-place modification
# - Left / Right, Start / End hints

# ------------------------------------------------------------
# TYPE 1: OPPOSITE ENDS (LEFT / RIGHT)
# ------------------------------------------------------------
# Pointers start at both ends and move inward.

# Example: Reverse array in-place
arr_example = [1, 2, 3, 4]

l = 0
r = len(arr_example) - 1

while l < r:
    arr_example[l], arr_example[r] = arr_example[r], arr_example[l]
    l += 1
    r -= 1

# Time: O(n)
# Space: O(1)

# ------------------------------------------------------------
# TYPE 2: SAME DIRECTION (FAST / SLOW)
# ------------------------------------------------------------
# Used for filtering, removing elements, compression.

# Example: Move non-zero elements forward
arr_example = [0, 1, 0, 3, 12]

slow = 0
for fast in range(len(arr_example)):
    if arr_example[fast] != 0:
        arr_example[slow] = arr_example[fast]
        slow += 1

# ------------------------------------------------------------
# IMPORTANT RULES
# ------------------------------------------------------------
# - Always move pointers conditionally
# - Never use extra space unless allowed
# - Index-based logic is mandatory
# - Sorted array + pair problem = two pointers
