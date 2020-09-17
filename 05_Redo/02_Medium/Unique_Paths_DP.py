"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the
bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example 1:
Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
Example 3:

Input: m = 7, n = 3
Output: 28
Example 4:

Input: m = 3, n = 3
Output: 6
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

    	# Create a dp of size m x n 
    	dp = [[1]*n for _ in range(m)]

    	# Start from the row+1 and col+1 coordinate in dp.
    	# Logic: Number of ways to arrive at current position in dp is value above position + value left of position
    	for i in range(1, len(dp)):
    		for j in range(1, len(dp[0])):
    			# Present value = Previous value in row + previous value in col
    			dp[i][j] = dp[i-1][j] + dp[i][j-1]


    	# The last value will have the total number of ways the robot can arrive to its destination. 
    	return dp[-1][-1]