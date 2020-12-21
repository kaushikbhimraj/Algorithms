"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		res = []
		# Check if the nums array exists. 
		if not nums:
			return res

		# Use a recursive helper to populate all possible permutations. 
		self.helper(res, nums, [])
		return res

	def helper(self, res, nums, curr):
		if not nums:
			res.append(curr[:])
			return 

		for i in range(len(nums)):
			self.helper(res, nums[:i] + nums[i+1:], curr+[nums[i]])