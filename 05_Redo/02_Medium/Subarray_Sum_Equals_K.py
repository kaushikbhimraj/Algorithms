"""
Given an array of integers and an integer k, you need to find the total number 
of continuous sub-arrays whose sum equals to k.
k = 7
nums = [3, 4, 7, 2, -3, 1, 4, 2]
"""

class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:

		# sum for zero will always be initalized.
		cache = dict()
		cache[0] = 1
		total = 0
		count = 0

		# Traverse array and check the subtraction of sum and k is in the cache
		for i in range(len(nums)):
			# sum elements from array each iteration
			total += nums[i]
			count += cache.get(total-k, 0)
			cache[total] = cache.get(total, 0) + 1

		return count
