"""
Imagine a robot sitting on the upper left corner of grid with r rows and c columns. The robot can 
only move in two directions, right and down, but certain cells are "off limits" such that the robot
cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom
right. 

Time Complexity:  O(mn)
Space Complexity: O(mn)
"""

class Solution:
	def __init__(self):
		self.memo = None

	# Using recursion and memoization. 
	def uniquePaths(self, m: int, n: int):

		# Create a 2-D array to store all paths. 
		self.memo = [[0]*n for _ in range(m)]
		return self.helper(m-1, n-1)

	def helper(self, row, col):
		# Bounding condition.
		if row < 0 or col < 0:
			return 0

		# Check if path is already visited. 
		if self.memo[row][col] > 0:
			return self.memo[row][col]

		# If traversal reaches origin then you found a new path.
		if row == 0 or col == 0:
			return 1

		# Main recursion. 
		self.memo[row][col] = self.helper(row-1, col) + self.helper(row, col-1)

		return self.memo[row][col]


	# Using dynamic programming
	def helperDP(self, row, col):

		# Create the DP table
		dp = [[1]*col for _ in range(row)]
		for i in range(1, row):
			for j in range(1, col):
				dp[i][j] = dp[i-1][j] + dp[i][j-1]

		return dp[-1][-1]

row, col = 7,3
x = Solution()
print("using resursion:    ", x.uniquePaths(row, col))
print("using dynamic prog: ", x.helperDP(row, col))