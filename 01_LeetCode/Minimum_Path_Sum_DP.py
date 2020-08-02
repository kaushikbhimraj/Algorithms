"""
Given a m x n grid filled non-negative numbers , find a path from to left to bottom
right which minimizes the sum of all numbers along its path. 

Note: You can only move either down or right at any point in time. 

Example:

Input:
[
[1,3,1],
[1,5,1],
[4,2,1]
]

Output: 7

Explanation: Because the path 1-> 3 -> 1 -> 1 -> 1 -> 1 minimizes the sum. 

"""

class Solution:
	def minPathSum(self, grid):

		# Base case
		if not grid or len(grid) == 0:
			return 0

		dp = [[0]*len(grid[0]) for _ in range(len(grid))]

		for row in range(len(grid)):
			for col in range(len(grid[0])):
				dp[row][col] += grid[row][col]

				# Now in the same position in dp, you want to look at the previous values
				if row > 0 and col > 0:
					dp[row][col] += min(dp[row - 1][col], dp[row][col - 1])

				elif row > 0:
					dp[row][col] += dp[row-1][col]

				elif col > 0:
					dp[row][col] += dp[row][col-1]

		return dp[-1][-1]


a = [[1,3,1],[1,5,1],[4,2,1]]


x = Solution()
print(x.minPathSum(a))