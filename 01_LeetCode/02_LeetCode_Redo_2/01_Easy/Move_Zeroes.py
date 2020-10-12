"""
Given an array nums, write a function to move all 0's to the end of it while maintaining 
the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

# Time: O(n)
# Space: O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        # Initialize value to count zeros
        countZeros = 0
        i = 0 
        
        # Traverse array and remove all zeros
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                countZeros += 1
            else:
                i += 1
                
        # Append all zeros to the end. 
        nums[:] = nums + [0]*countZeros
        