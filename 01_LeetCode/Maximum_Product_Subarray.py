"""
Given an integer array nums, find the contiguous subarray within an array (containing 
at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""

class Solution:
	def maxProduct(self, nums):

		# Edge case to check if nums exists. 
		if not nums or len(nums) == 0:
			return 0

		# Keep track of the maximum product. 
		max_product = max(nums)

		# Create a dp table. 
		dp = [[0]*len(nums) for _ in range(len(nums))]

		# Numbers that are not multiplied and are stand alone will be left same. 
		for i in range(len(nums)):
			dp[i][i] = nums[i]

		# Populate dp table using specific logic
		# [2, 6, 0, 0]
		# [0, 0, 0, 0]
		# [0, 0, 0, 0]
		# [0, 0, 0, 4]
		for i in range(len(nums)-1):
			for j in range(1, len(nums)):

				product = dp[i+1][j] * dp[i][j-1]
				dp[i][j] = product if product > 0 else 0
				max_product = max(product, max_product)

		for row in range(len(dp)):
			print(dp[row])
		return max_product

a = [2,3,-2,4]

x = Solution()
x.maxProduct(a)