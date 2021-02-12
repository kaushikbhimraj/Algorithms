"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is 
equal to the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array 
(including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space 
for the purpose of space complexity analysis.)

T: O(n); S: O(n)
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        fwd = [1] * n
        rev = [1] * n
        
        i = 1
        while (i < n):
            fwd[i] = nums[i-1] * fwd[i-1]
            i += 1
        
        i = n - 2
        while (i >= 0):
            rev[i] = nums[i+1] * rev[i+1]
            i -= 1
        
        for i in range(n):
            nums[i] = fwd[i] * rev[i]
        
        return nums