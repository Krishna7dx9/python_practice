# ============================================================
# Pattern: Two Pointers (canonical opposite-direction)
# ============================================================

# Problem: 977. Squares of sorted array
# LeetCode: https://leetcode.com/problems/squares-of-a-sorted-array/description/
# Key Insight / Pattern Notes: Two Pointer (canonical opposite-direction) 
# Difficulty: Easy
# ------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(n)
# Notes / Observations: 
# ============================================================

class Solution(object):
    def sortedSquares(self, nums):
        left = 0
        right = len(nums) - 1
        n = len(nums)
        write_idx = len(nums) - 1           # Position to write next largest square
        result = [0] * n
        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                result[write_idx] = nums[left] * nums[left] 
                left += 1
                write_idx -=1
            else:
                result[write_idx] = nums[right] * nums[right] 
                right -= 1
                write_idx -=1
        return result

# ------------------------------------------------------------
# Example Usage / Test Cases (optional)
# ------------------------------------------------------------
if __name__ == "__main__":
    nums = [-7,-3,2,3,11]
    solution = Solution()           # Creating instance
    result = solution.sortedSquares(nums)
    print(result)

"""
Dry run:

Problem: 977. Squares of sorted array
Pattern: Two Pointer (Opposote Direction, left/right)

Given: 
Array - nums
Sorted in incresing order

Return:
Array of the square of each number

Role:
left  → Starts from beggining
right → Starts from end

Initial Values:
Input - nums = [-7,-3,2,3,11]
left = 0
right = 4
n = len(nums)
result = [0] * n             # Allocate an array of size n filled with zeros so we can overwrite values by index.
write_idx = len(nums) - 1

Action Condition: 
if abs(nums[left]) >= abs(nums[right]):
    result[write_idx] = nums[left] * nums[left] 
    left += 1
    write_idx -=1
    else:
        result[write_idx] = nums[right] * nums[right]
        right -= 1
        write_idx -=1
return sqr_arr

Running codition: WHile left <= right
Stopping Condition: When left > right

Tracing table:
nums = [-7,-3,2,3,11]

step | left | right | nums[left] | nums[right] | condition | action    | sqr_arr
1       0      4          -7          11           False     else part   [0, 0, 0, 0, 121]
2       0      3          -7           3           True      if part     [0, 0, 0, 49, 121]
3       1      3          -3           3           True      if part     [0, 0, 9, 49, 121]
4       2      3           2           3           False     else part   [0, 9, 9, 49, 121]
5       2      2           2           2           True      if part     [4, 9, 9, 49, 121]                      

Final outcome: [4, 9, 9, 49, 121]

"""