"""
Given an array nums of n integers where n > 1,  return an array output such that 
output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix 
of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count 
as extra space for the purpose of space complexity analysis.)
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #         [01, 02, 03, 04]
        # left -> [01, 01, 02, 06]
        #         [24, 12, 04, 01] -> right
        
        # Create two arrays of same size as nums. 
        # Populate '1's in the arrays. 
        left = [1]*len(nums)
        right = [1]*len(nums)
        
        # Iterate from left. 
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
        
        # Iterate from right.
        for j in reversed(range(len(nums)-1)):
            right[j] = right[j+1] * nums[j+1]
        
        # Multiply the left and right in place for nums array.
        for k in range(len(nums)):
            nums[k] = left[k] * right[k]
            
        return nums