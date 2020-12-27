"""
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally 
or vertically. You may assume all four edges of the grid are all surrounded by water.
 
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
class Solution:
    def numIslands(self, grid):
        # Iterate through grid and implement DFS (change visited node to 0)
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.helper(grid, i, j)
                    islands += 1
        return islands
    
    def helper(self, grid, i, j):
        if i < 0 or i > len(grid)-1 or j <0 or j > len(grid[0])-1 or grid[i][j] == "0":
            return 
        grid[i][j] = "0"
        self.helper(grid, i+1, j)
        self.helper(grid, i-1, j)
        self.helper(grid, i, j+1)
        self.helper(grid, i, j-1)