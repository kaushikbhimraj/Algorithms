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

	# This particular two sum method sorts the array in place and
	# changes the index values of the array. It might good to do for a problem 
	# But for leetcode this will mess up the output and will always be wrong. 
	# This will work for three sum. 
	def twoSum(self, nums, target):
		nums.sort()
		l  = 0
		r = len(nums) - 1

		while l < r:

			x = nums[l]
			y = nums[r]

			if l > 0 and x == nums[l-1]:
				l += 1

			elif r < len(nums)-1 and y == nums[r+1]:
				r -= 1

			else:
				if x+y == target:
					print(l, r)
					r -= 1
					l += 1
					# return [l, r]
				elif x+y > target:
					r -= 1
				else:
					l += 1




a = [-4, -1, -1, 0, 1, 2]
b = [0, 2, 4, 5, 7, 12]
x = Solution()
x.twoSum(a, 1)

