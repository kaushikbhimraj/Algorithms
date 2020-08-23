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
        
        # Create two empty array of length nums. 
        left = [0]*len(nums)
        right = [0]*len(nums)
        
        # Set the first value of left array == 1
        # Set the last value of right array == 1
        left[0] = 1
        right[-1] = 1
        
        results = []
        # Traverse left array from left to right 
        # Populate each element with left[i] = left[i-1]*nums[i-1]
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
        
        # Traverse right array from right to left. 
        # Populate each element with right[j] = right[j+1]*nums[j+1]
        for j in range(len(nums)-2, -1, -1):
            right[j] = right[j + 1] * nums[j + 1]
        
        # Loop one last time, multiply each element in left with each element in right. 
        for k in range(len(nums)):
            results.append(left[k] * right[k])
            
        return results


# JAVA_HOME C:\jdk-13.0.1
# PATH C:\jdk-13.0.1\bin