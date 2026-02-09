# Problem: 344. Reverse String
# LeetCode: https://leetcode.com/problems/reverse-string/
# Key Insight / Pattern Notes: Two Pointers (left, right)
# Difficulty: Easy
# ------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# Notes / Observations: Using temporary variable to swap values.
# ============================================================

class Solution(object):
    def reverseString(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            x = s[left]
            s[left] = s[right]
            s[right] = x
            left += 1
            right -= 1
        
# Example Usage / Test Case
if __name__ == "__main__":
    s = "Hello"                 
    s = list(s)
    Solution().reverseString(s)
    print(s)  # Expected: ["o", "l", "l", "e", "H"]
