# ============================================================
# PROBLEM PATTERNS — TWO POINTERS
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
from typing import Any


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

# ============================================================
# ARRAY PROBLEM PATTERNS — TWO POINTERS
# Leetcode (PYTHON)
# ============================================================

# ============================================================
# Pattern: Two Pointers
# ============================================================

# Problem: 283. Move Zeroes
# LeetCode: https://leetcode.com/problems/move-zeroes/
# Key Insight / Pattern Notes: Two Pointers (Fast/Slow)
# Difficulty: Easy
# ------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# Notes / Observations: Slow tracks position to place non-zero, fast scans
# ============================================================

class Solution(object):
    def moveZeroes(self, nums):
        slow = 0
        for f in range(len(nums)):
            if nums[f] != 0:
                nums[slow] = nums[f]
                slow += 1
        for s in range(slow, len(nums)):
            nums[s] = 0

# Example Usage / Test Case
if __name__ == "__main__":
    nums = [0,1,0,3,12]
    Solution().moveZeroes(nums)
    print(nums)  # Expected: [1,3,12,0,0]

# ============================================================
# Pattern: Two Pointers
# ============================================================

# Problem: 344. Reverse String
# LeetCode: https://leetcode.com/problems/reverse-string/
# Key Insight / Pattern Notes: Two Pointers (left, right)
# Difficulty: Easy
# ------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# Notes / Observations: 
# ============================================================

class Solution_(object):
    def reverseString(self, s):
        left = 0
        right = len(s) - 1
        while not left >= right:
            x = s[left]
            s[left] = s[right]
            s[right] = x
            left += 1
            right -= 1
        
# Example Usage / Test Case
if __name__ == "__main__":
    s = "Hello"
    s = list(s)
    Solution_().reverseString(s)
    print(s)  # Expected: ["o", "l", "l", "e", "H"]

"""
============================================================
ARRAY PROBLEM PATTERNS — TWO POINTERS
INTERVIEW-READY SINGLE FILE (PYTHON)
============================================================

Rules Followed:
- Optimal time complexity
- No unnecessary extra space
- Index-based pointer logic
- Clear interview-style questions
"""

# ============================================================
# 1. Reverse Array In-Place
# Question:
# Reverse the array without using extra space.
# ============================================================

def reverse_array(arr):
    l, r = 0, len(arr) - 1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    return arr


# ============================================================
# 2. Check Palindrome (String)
# Question:
# Return True if string is palindrome.
# ============================================================

def is_palindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


# ============================================================
# 3. Two Sum II (Sorted Array)
# Question:
# Return 1-based indices of two numbers whose sum = target.
# ============================================================

def two_sum_sorted(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        curr = nums[l] + nums[r]
        if curr == target:
            return [l + 1, r + 1]
        elif curr < target:
            l += 1
        else:
            r -= 1
    return []


# ============================================================
# 4. Remove Duplicates from Sorted Array
# Question:
# Modify array in-place and return new length.
# ============================================================

def remove_duplicates(nums):
    if not nums:
        return 0

    slow = 1
    for fast in range(1, len(nums)):
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1
    return slow


# ============================================================
# 5. Move Zeroes
# Question:
# Move all zeroes to the end maintaining order.
# ============================================================

def move_zeroes(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    return nums


# ============================================================
# 6. Remove Element
# Question:
# Remove all occurrences of val in-place.
# ============================================================

def remove_element(nums, val):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    return slow


# ============================================================
# 7. Squares of a Sorted Array
# Question:
# Return sorted squares in O(n) time.
# ============================================================

def sorted_squares(nums):
    n = len(nums)
    res = [0] * n
    l, r = 0, n - 1
    pos = n - 1

    while l <= r:
        if abs(nums[l]) > abs(nums[r]):
            res[pos] = nums[l] * nums[l]
            l += 1
        else:
            res[pos] = nums[r] * nums[r]
            r -= 1
        pos -= 1

    return res


# ============================================================
# 8. Container With Most Water
# Question:
# Find max water container area.
# ============================================================

def max_area(height):
    l, r = 0, len(height) - 1
    max_water = 0

    while l < r:
        width = r - l
        water = min(height[l], height[r]) * width
        max_water = max(max_water, water)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_water


# ============================================================
# 9. Trapping Rain Water
# Question:
# Calculate trapped rainwater using two pointers.
# ============================================================

def trap(height):
    l, r = 0, len(height) - 1
    left_max = right_max = 0
    water = 0

    while l < r:
        if height[l] < height[r]:
            left_max = max(left_max, height[l])
            water += left_max - height[l]
            l += 1
        else:
            right_max = max(right_max, height[r])
            water += right_max - height[r]
            r -= 1

    return water


# ============================================================
# 10. 3Sum
# Question:
# Return all unique triplets that sum to zero.
# ============================================================

def three_sum(nums):
    nums.sort()
    res = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1

    return res


# ============================================================
# END OF TWO POINTERS PATTERN FILE
# ============================================================