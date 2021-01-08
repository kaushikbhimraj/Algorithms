"""
Given a m x n grid filled with non-negative numbers, find a path from top left to 
bottom right which minimizes the sum of all numbers along its path.

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

    # Create a new dp matrix of the same size as original matrix. 
    # You could perform the same operation in place in original array.
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Create dp matrix 
        dp = [[0]*len(grid[0]) for _ in range(len(grid))]
        dp[0][0] = grid[0][0]
        

        # Core logic of dp is, to add the minimum sum from up and down to the current value in grid. 
        for row in range(1, len(dp)):
            dp[row][0] = dp[row-1][0] + grid[row][0]
        
        for col in range(1, len(dp[0])):
            dp[0][col] = dp[0][col-1] + grid[0][col]
        
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])
        
        # Last value in dp array will have the minimum path sum. 
        return dp[-1][-1]