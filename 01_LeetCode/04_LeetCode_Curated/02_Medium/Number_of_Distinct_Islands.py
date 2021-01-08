"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing 
land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of 
the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if 
and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.
Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
Note: The length of each dimension in the given grid does not exceed 50.
"""

class Solution:
    def __init__(self):
        self.islands = set()
        self.directions = ""
        
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        # Helper function to perform DFS. 
        def findLand(x, y, d):
            if x < 0 or x > len(grid)-1 or y < 0 or y > len(grid[0])-1 or grid[x][y] != 1:
                return
            
            grid[x][y] = -1
            self.directions += d

            findLand(x+1, y, "d")
            findLand(x-1, y, "u")
            findLand(x, y+1, "r")
            findLand(x, y-1, "l")

            # Most important part of this logic is the "b" direction. In thre recursive stack, 
            # if don't capture the back direction, we won't be able to establish distinct islands 
            # Two islands might have the same number of 1s their shapes are different. 
            self.directions += "b"
        
        # Whenever you find a 1, DFS using findLand. 
        # DFS will populate the string with directions. 
        # Add it to set and clear string. 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    findLand(i, j, "o")
                    self.islands.add(self.directions)
                    self.directions = ""
        
        return len(self.islands)