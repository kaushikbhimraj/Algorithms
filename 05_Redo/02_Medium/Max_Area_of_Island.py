"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) 
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid 
are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum 
area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 
4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""

# Straight forward case of backtracking. 
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Visit a value and count all neighbors of '1' (Use DFS)
        # Track max count in each iteration
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    result = max(result, self.backTrack(grid, i, j))
                    
        # Return 0 if no islands are found. 
        return result if (result != 0) else 0
        
    # Helper function. 
    # Most important part is to change visited value to 0.
    def backTrack(self, grid, i, j) -> int:
        
        # Set base case to not exceed array boundary and current value is '1'. 
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j]:
            grid[i][j] = 0
            return 1 + self.backTrack(grid, i-1, j) + self.backTrack(grid, i+1, j) \
        + self.backTrack(grid, i, j-1) + self.backTrack(grid, i, j+1)
        return 0