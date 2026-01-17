# ============================================================
# DSA — TIME ↔ SPACE TRADE-OFFS (RED-FLAG DRIVEN DECISIONS)
# ============================================================

# This file explains WHEN and WHY to trade
# TIME for SPACE or SPACE for TIME in interviews.

# ============================================================
# RULE 0: WHAT A TRADE-OFF IS
# ============================================================

# Trade-off = Improving one resource
# (Time or Space) by sacrificing the other.

# In DSA:
# Trade-off is ALWAYS between Time ↔ Space

# ============================================================
# RULE 1: INTERVIEW PRIORITY
# ============================================================

# 1) Correct solution
# 2) Optimize TIME
# 3) Trade SPACE if needed
# 4) Optimize SPACE only if asked or constrained

# ============================================================
# SECTION 1: RED FLAGS THAT TRIGGER TIME → SPACE TRADE-OFF
# (Use EXTRA SPACE to REDUCE TIME)
# ============================================================

# RED FLAG 1: Nested loops
# --------------------------------
# for i in range(n):
#     for j in range(n):
#
# Problem:
# Time = O(n^2)
#
# Trade-off Action:
# Use hash set / hash map
#
# Result:
# Time: O(n)
# Space: O(n)


# RED FLAG 2: Searching inside loops
# --------------------------------
# for x in arr:
#     if x in arr:
#
# Problem:
# Repeated O(n) search
#
# Trade-off Action:
# Convert list → set / dict
#
# Result:
# Time: O(1) lookup
# Space: O(n)


# RED FLAG 3: Recomputing same values
# --------------------------------
# sum(arr[:i]) inside loop
#
# Problem:
# Same computation repeated
#
# Trade-off Action:
# Prefix sum / precomputation
#
# Result:
# Time: O(n)
# Space: O(n)


# RED FLAG 4: Pairwise comparisons
# --------------------------------
# for i in range(n):
#     for j in range(i+1, n):
#
# Problem:
# Too many comparisons
#
# Trade-off Action:
# Sorting OR hashing
#
# Result:
# Time: O(n log n) or O(n)
# Space: O(1) or O(n)


# RED FLAG 5: Recursive solution with overlapping work
# --------------------------------
# f(n-1) repeatedly
#
# Problem:
# Repeated subproblems
#
# Trade-off Action:
# Memoization / DP table
#
# Result:
# Time improves
# Space increases


# ============================================================
# SECTION 2: RED FLAGS THAT TRIGGER SPACE → TIME TRADE-OFF
# (Use EXTRA TIME to REDUCE SPACE)
# ============================================================

# RED FLAG 6: Large auxiliary data structures
# --------------------------------
# Using extra arrays, dicts, sets
#
# Problem:
# High memory usage
#
# Trade-off Action:
# In-place algorithm
#
# Result:
# Space: O(1)
# Time: Same or worse


# RED FLAG 7: Recursion depth growing linearly
# --------------------------------
# f(n-1)
#
# Problem:
# Call stack space = O(n)
#
# Trade-off Action:
# Convert recursion → iteration
#
# Result:
# Space: O(1)
# Time: Same


# RED FLAG 8: Slicing / copying data
# --------------------------------
# arr[:i], arr[1:], arr[mid:]
#
# Problem:
# Hidden O(n) space
#
# Trade-off Action:
# Use index pointers
#
# Result:
# Space: O(1)
# Time: Same


# RED FLAG 9: Storing full DP table
# --------------------------------
# dp = [0] * n
#
# Problem:
# Unnecessary memory usage
#
# Trade-off Action:
# Rolling variables
#
# Result:
# Space: O(1)
# Time: Same


# ============================================================
# SECTION 3: DECISION CHECKLIST (INTERVIEW)
# ============================================================

# Ask yourself:
# - Is TIME too slow?
# - Is SPACE too large?
# - Is input size large?
# - Is in-place required?

# Default decision:
# Optimize TIME first.

# ============================================================
# SECTION 4: INTERVIEW JUSTIFICATION TEMPLATES
# ============================================================

# "I am trading extra space to reduce time complexity."

# "This solution is in-place and optimizes space
# at the cost of additional computation."

# "Given the constraints, this trade-off is optimal."

# ============================================================
# ONE-LINE RULE (MEMORIZE)
# ============================================================

# Every red flag must trigger a conscious
# time ↔ space trade-off decision.
