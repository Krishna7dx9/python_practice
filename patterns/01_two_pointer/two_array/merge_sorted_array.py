class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j  = n - 1
        write = m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[write] = nums1[i]
                i -= 1
                write -= 1
            else:
                nums1[write] = nums2[j]
                j -= 1
                write -= 1

if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    Solution().merge(nums1, m, nums2, n)
    print(nums1)

"""
Problem: Merge Sorted Array
Pattern: Two Pointer (Write from end) 

Given:
Arrays, num1, num2
Integers Representing number of element in arrays: m, n
len(num1) - (m + n)                # last n positions are buffer
len(num2) - n
num1 has the length of (m + n), where first m elements denote the elements denote the element that should
be merged, and the last n elements are set to 0 and should be ignored.

Must Do:
Merge num1 and num2 in increasing order
Do not return this merged array, instead store it inside num1

Pointers:
i = m - 1
j  = n - 1
write = m + n - 1

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3

Initially:
m = 3
n = 3
i =  2
j = 2
write = 5

Condition:
while j >= 0:
    if i >= 0 and nums1[i] >= nums2[j]:
        nums1[write] = nums1[i]
        i -= 1
        write -= 1
    else:
        nums1[write] = nums2[j]
        j -= 1
        write -= 1


step | i | j | nums1[i] | nums2[j] | condition | action            | nums1 state
1      2   2      3          6       else True   write 6, j -= 1     [1,2,3,0,0,6]
2      2   1      3          5       else True   write 5, j -= 1     [1,2,3,0,5,6]      
3      2   0      3          2       if True     write 3, i -= 1     [1,2,3,3,5,6]
4      1   0      2          2       if True     write 2, i -=1      [1,2,2,3,5,6]

Final outcome: [1,2,2,3,5,6]
"""


