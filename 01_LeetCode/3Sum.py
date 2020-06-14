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
	class Solution:

	def threeSum(self, nums):
		zero_sum = []
		nums.sort()
		# print(nums)
		i = 0

		for i in range(len(nums)-2):

			# We do not need to consider i after nums[i]>0, since sum of 3 positive will be always greater than zero. [7]
			if nums[i] > 0:
				break
			if i > 0 and nums[i] == nums[i-1]:
				continue

			l, r = i+1, len(nums)-1
			while l < r:

				three_sum = nums[i] + nums[l] + nums[r]

				if three_sum == 0:
					zero_sum.append([nums[i], nums[l], nums[r]])

					# We need to move the left and right pointers to the next different numbers, so we do not get repeating result.
					while l < r and nums[l] == nums[l+1]:
						l += 1
					while l < r and nums[r] == nums[r-1]:
						r -= 1
					l += 1
					r -= 1
				elif three_sum > 0:
					r -= 1
				else:
					l += 1

		return zero_sum




# Unit Test Cases
a=[-1,0,1,2,-1,-4]
b=[]
c=[-1]
d=[2,2,2]
e=[0,0,0]
f=[-9, 2, 2, 7, 10, 13]
g=[0, 0, 0, 0]
h=[-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]

x = Solution()
print(x.threeSum(a))

