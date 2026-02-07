class Solution(object):
    def isPalindrome(self, s):
        s = "".join(c for c in s.lower() if c.isalnum())  # clean string
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:  # mismatch
                return False
            left += 1
            right -= 1

        return True
