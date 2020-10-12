"""
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide 
and conquer approach, which is more subtle.

"""

class Solution:

	# Brute force -> O(n**2) -> TLE
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Declare the max sum to be first value of the array
        max_sum = nums[0]
        
        # Loop through every value and compute sum for each combination
        for i in range(len(nums)):
            
            # asum is the temporary sum of each value after i. 
            asum = nums[i]
            
            # Take the max of the two values before the inner loop as length of array might be 1. 
            # Maximum sum is tracked and returned in max_sum 
            max_sum = max(max_sum, asum)
            for j in range(i+1, len(nums)):
                asum += nums[j]
                max_sum = max(max_sum, asum)
        
        return max_sum

    # Dynamic programming -> Time: O(n) Space: O(n)
    def maxSubArray_dp(self, nums: List[int]) -> int:

    	# Make sure length of nums is greater than 1. 
    	if len(nums) == 1:
    		return nums[0]
        
        # Create an array of the same length as nums
        dp = [0]*len(nums)
        dp[0] = nums[0]
        
        # Track maximum sum
        maxvalue = 0
        
        # Start from the second element,
        # Check if value in dp[i-1] + nums[i] > nums[i] (Consider on the max)
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            maxvalue = max(maxvalue, dp[i])
        
        return maxvalue

    # In place dynamic programming -> Time: O(n) Space: O(1)
    def maxSubArray_dp_inplace(self, nums: List[int]) -> int:  
        if len(nums) == 1:
            return nums[0]
        
        maxvalue = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1]+nums[i], nums[i])
            maxvalue = max(maxvalue, nums[i])
        
        return maxvalue