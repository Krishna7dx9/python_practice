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