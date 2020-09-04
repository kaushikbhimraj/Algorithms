"""
Given an array of n positive integers and a positive integer s, find the minimal 
length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 
0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the 
time complexity is O(n log n). 
"""

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:

    	# Create variable to store length
    	result = float("inf")

    	# Left pointer
    	left = 0

    	# Variable to track a running sum
    	val_sum = 0


    	# Loop through each element and update running sum
    	for i in range(len(nums)):
    		val_sum += nums[i]

    		# If the val_sum is equal or has exceed the target value of s. 
    		# Update the results with the min length
    		# Rather than zeroing out val_sum, remove the value at left pointer. 
    		# Move the pointer to the next value. 
    		while (val_sum >= s):
    			result = min(result, i+1-left)
    			val_sum -= nums[left]
    			left += 1

    	# Return result if it is not inf else return 0
    	return result if result != float("inf") else 0
