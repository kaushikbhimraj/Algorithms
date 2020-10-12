"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # Edge case
        if not nums or len(nums) == 0:
            return 0
        
        result = 1
        # Create a dp table to hold all the previous results 
        dp = [1]*len(nums)
        
        # Populate the dp array
        for i in range(1, len(nums)):
            maxvalue = 0
            
            # Every time i changes check all values before it are lower than its value. 
            for j in range(i):
                if nums[i] > nums[j]:
                    # Consider the max value in the dp table and store it maxvalue. 
                    maxvalue = max(maxvalue, dp[j])
            
            # Update dp table with maxvalue and 1. 
            dp[i] = 1 + maxvalue
            
            # Keep track of the max value each iteration. 
            result = max(result, dp[i])
        
        # Return the max sequence
        return result