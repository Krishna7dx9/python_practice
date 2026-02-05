# ============================================================
# Pattern: Two Pointers 
# ============================================================

# Problem: Remove Element
# LeetCode: https://leetcode.com/problems/remove-element/description/
# Key Insight / Pattern Notes: Two Pointer (Same Direction Pointer - read/write)
# Difficulty: Easy
# ------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# Notes / Observations: fast pointer scans the array so the condition should be applied to fast pointer, not slow
# ============================================================

class Solution(object):
    def removeElement(self, nums, val):
        if not nums:
            return 0
            
        slow = 0

        for fast in range(0, len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1   
        return slow

# ------------------------------------------------------------
# Example Usage / Test Cases (optional)
# ------------------------------------------------------------
if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 3
    solution = Solution()       # creating instance
    k = solution.removeElement(nums, val)
    print(k)


"""
Question Dry run:

Problem: Remove Elements
Pattern: Two pointer (Same direction pointers - read/write)

Given:
 array: nums
 integer: val

Must do:
-Remove all occurence of val in nums
-Consider len(elements in nums which are not equal to val) to be k.
-change the array nums to the array in which first k elements in the nums is not equal to val, and
 Elements after k are irrelevant junk

Method:
In-place

Return:
k - len(elements in nums which are not equal to val)

slow - represents next write index (How many valid element written so far)
fast - Scans array

Input: [3,2,2,3],    val = 3
slow idx = 0
fast idx = 0

Action Condition: if nums[fast idx] != val:
                      nums[slow idx] = nums[fast idx]        # copying fast value into slow
                      slow idx += 1
                                
Loop stops when: fast == len(nums)

step | slow idx | fast idx | nums[slow idx] | nums[fast idx] | condition - nums[fast idx] != val | action     | array state
1       0           0           3             3                False                                Nothing      [3,2,2,3]
2       0           1           3             2                True                             copy, slow += 1  [2,2,2,3]
3       1           2           2             2                True                             copy, slow +=    [2,2,2,3]
4       2           3           2             3                False                                Nothing      [2,2,2,3]

Final outcome: [2, 2, 2, 3]
Return: k = slow idx = 2
"""