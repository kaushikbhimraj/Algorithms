"""
Given an integer array nums, find the contiguous subarray within an array (containing at 
least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # Have to find the combo chain that give the max product. 
        # Three scenarios here, 
        
        # Case 1: 
        # If all numbers are positive, you can simply multiply all intergers to
        # get the maximum integer. 
        
        # Case 2:
        # If there is a zero, the combo will be broken and you will to start 
        # a new combo and you can use a variable like 'result' to keep track of
        # max product. 
        
        # Case 3:
        # When there is a negative number, it can change the product from 
        # highese number to lowest number in one operation. This is where
        # tracking the minimum number comes into play. 
        
        # Initialize variables to store running min and max. 
        # Initialize variable to store overall max product. 
        curr_min = nums[0]
        curr_max = nums[0]
        result = curr_max
        
        # Start from the second element in array, since first is already part of the product. 
        for i in range(1, len(nums)):
            
            # Min and max is calculated using
            # (current_value, curr_max * current_value, curr_min * current_value)
            # But the max is first stored in a temp variable NOT TO AFFECT THE MIN calculation. 
            temp = max(nums[i], nums[i] * curr_max, nums[i] * curr_min)
            curr_min = min(nums[i], nums[i] * curr_max, nums[i] * curr_min)
            
            curr_max = temp
            
            result = max(curr_max, result)
        
        return result