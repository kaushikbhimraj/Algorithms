"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution:

	# The current solution does not account for repeatitions of zero sum sets. 
	# The way to avoid repeititions is by checking if the next element is same. 
	# These repetitions need to be checked twice. 
	# 			- Once when iterating through nums. 
	# 			- Again inside the two sum loop. 
	def threeSum(self, nums):

		# create an array to store all sub-arrays that are zero sums. 
		zero_sums = []

		# Sort the array in place using Python's in-built Tim Sort
		nums.sort()

		# Using a FOR loop, iterate the entire array. 
		for i in range(len(nums)):
			if i > 0 and nums[i] == nums[i-1]:
				continue

			# Create two pointers for the left and right
			l = i+1
			r = len(nums)-1

			# Using a while loop, excute two to find the pair of numbers that compute a target sum of zero. 
			while l < r:

				compute_sum = nums[i] + nums[l] + nums[r]

				if compute_sum == 0:
					zero_sums.append([nums[i], nums[l], nums[r]])

					# Increment/decrement when the next elements are the same. 
					while l < r and nums[l] == nums[l+1]: 
						l += 1
					while r > l and nums[r] == nums[r-1]:
						r -= 1
					l += 1
					r -= 1

				elif compute_sum > 0:
					r -= 1

				else:
					l += 1
		return zero_sums


nums = [-1, 0, 1, 2, -1, -4]

x = Solution()
print(x.threeSum(nums))