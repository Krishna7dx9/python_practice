# Problem: 26. Remove Duplicates from Sorted Array
# LeetCode: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Key Insight / Pattern Notes: Two Pointers (Same Direction / Read–Write)
# Difficulty: Easy
# ------------------------------------------------------------
# Time Complexity: O(n) 
# Space Complexity: O(1)
# Notes / Observations: In two pointer we using copying not removing elements  
# =======================================================

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
                return 0
                
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1


if __name__ == "__main__":
    nums = [0, 1, 2, 2, 3, 3, 4, 4]
    solution = Solution()           # creating instance
    k = solution.removeDuplicates(nums)
    print(k)