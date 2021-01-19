"""
Given an integer array, nums, return the total number of "partners" in the array. 

Note: Two numbers in our array are partners if they reside at different indices and both contain 
the same value. 

Given the following array nums...
nums = [5, 5, 3, 1, 1, 3, 3], return 5.
5 (index 0) and 5 (index 1) are partners.
1 (index 3) and 1 (index 4) are partners.
3 (index 2) and 3 (index 5) are partners.
3 (index 2) and 3 (index 6) are partners.
3 (index 5) and 3 (index 6) are partners.
"""

class Solution:
	def Partners(self, nums):
		mem = defaultdict(int)
		for i in range(len(nums)):
			mem[nums[i]] += 1

		count = 0
		for key in mem.keys():
			if (mem[key] % 2 == 0):
				count += 1
		return count