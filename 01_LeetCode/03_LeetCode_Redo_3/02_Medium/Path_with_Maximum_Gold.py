"""
In a gold mine grid of size m * n, each cell in this mine has an integer representing the amount of gold in 
that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position you can walk one step to the left, right, up or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
 

Example 1:
Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24

Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.

Example 2:
Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28

Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]

Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.

Constraints:
1 <= grid.length, grid[i].length <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.

T: O(4*3^n); S: O(n) where n is depth of recursion stack. 
"""

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        max_gold = [0]
        run_sum = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    self.dfs(i, j, grid, run_sum, max_gold)
        return max_gold[0]
    
    def dfs(self, i, j, grid, run_sum,  max_gold):
        if (i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1 or grid[i][j] == 0):
            return
        
        run_sum += grid[i][j]
        origin = grid[i][j]
        grid[i][j] = 0
        max_gold[0] = max(max_gold[0], run_sum)
        
        self.dfs(i+1, j, grid, run_sum, max_gold)
        self.dfs(i-1, j, grid, run_sum, max_gold)
        self.dfs(i, j+1, grid, run_sum, max_gold)
        self.dfs(i, j-1, grid, run_sum, max_gold)
        
        grid[i][j] = origin