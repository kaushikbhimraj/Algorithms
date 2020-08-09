"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you 
implement it using only constant extra space complexity?
"""


class Solution:
	def missingNumber(self, nums: List[int]) -> int:
		# Create a set and check if values exists in set. 

		# The loop should run for 1 extra than length for missing element. 
		nums_set = set(nums)
		for i in range(len(nums) + 1):
			if i not in nums_set:
				return i

    def missingNumber_bitManipulation(self, nums: List[int]) -> int:
        # XOR is 0 if elements are same. 
        missing = len(nums)
        for i in range(len(nums)):
            missing ^= i ^ nums[i]
        
        return missing