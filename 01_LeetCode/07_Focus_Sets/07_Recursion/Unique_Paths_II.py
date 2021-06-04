"""
# 63. Unique Paths II
A robot is located at the top-left corner of a m x n grid (marked 'Start' in 
the diagram below).

The robot can only move either down or right at any point in time. The robot is trying 
to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there 
be?

An obstacle and space is marked as 1 and 0 respectively in the grid.
"""

# Start from bottom to top. 
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.count = {}
        return self.helper(len(obstacleGrid)-1, len(obstacleGrid[0])-1, obstacleGrid)
        
    def helper(self, i, j, obstacleGrid):
        if (i < 0 or j < 0 or obstacleGrid[i][j] == 1):
            return 0
        
        if ((i, j) in self.count):
            return self.count[(i,j)]
        
        if (i == 0 and j == 0):
            return 1
        
        self.count[(i,j)] = self.helper(i-1, j, obstacleGrid) + self.helper(i, j-1, obstacleGrid)
        return self.count[(i,j)]
        