"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

"""

class Solution:
	def minPathSum(self, grid):

		# Edge case
		if not grid or len(grid) == 0:
			return 0

		# Creat the dp table for the grid
		dp = [[0]*len(grid[0]) for _ in range(len(grid))]

		# Populate the dp table with values using logic. 
		for i in range(len(grid)):
			for j in range(len(grid[0])):

				dp[i][j] += grid[i][j]

				if i > 0 and j > 0:
					dp[i][j] += min(dp[i-1][j], dp[i][j-1])

				if i > 0:
					dp[i][j] += dp[i-1][j]

				if j > 0:
					dp[i][j] += dp[i][j-1]

		return dp[-1][-1]
