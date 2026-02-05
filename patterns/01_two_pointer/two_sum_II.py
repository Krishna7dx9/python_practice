# Problem: 167. Two Sum II - Input Array Is Sorted
# LeetCode: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Key Insight / Pattern Notes: Two Pointers (left, right)
# Difficulty: Medium
# ------------------------------------------------------------
# Time Complexity: O(n) - loop depending on input size
# Space Complexity: O(1) - variable is constant
# Notes / Observations: 1. discarding impossible pairs using monotonicity
#                       2. monotocity - Because the array is sorted, increasing the left pointer increases
#                          the sum, and decreasing the right pointer decreases the sum—allowing a linear
#                          two-pointer search.
# ============================================================

class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

# Example Usage / Test Case
if __name__ == "__main__":
    num = [2, 7, 11, 15]
    target = 9
    solution = Solution()                 # create instance
    result = solution.twoSum(num, target)
    print(result)          # Expected: [1, 2]