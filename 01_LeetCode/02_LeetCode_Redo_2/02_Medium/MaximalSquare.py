
"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""

class Solution:
	def maximalSquare(self, matrix):

		# Max value
		max_value = 0

		# Creating the dp table from the matrix
		dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

		# Loop through all values in matrix
		for row in range(len(dp)):
			for col in range(len(dp[0])):

				# If value is greater than 0 then pick min of left, diagnal and top of current position
				if matrix[row][col] == "1":
					dp[row][col] = 1 + min(dp[row-1][col-1], dp[row-1][col], dp[row][col-1])
					max_value = max(max_value, dp[row][col])

		return max_value ** 2


a = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

x = Solution()
print(x.maximalSquare(a)).