"""
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1

"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """        
        
        # Would need a recursive call to change this in rows and columns. 
        # If in that path, you find another zero, skip it.
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    self.run(matrix, i, j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "a":
                    matrix[i][j] = 0
    
    def run(self, matrix, i, j):
        # Up 
        x, y = i, j
        for u in range(x-1, -1, -1):
            if matrix[u][y] != 0 and matrix[u][y] != "a":
                matrix[u][y] = "a"
        # Down
        x, y = i, j
        for d in range(x+1, len(matrix)):
            if matrix[d][y] != 0 and matrix[d][y] != "a":
                matrix[d][y] = "a"
        # Left 
        x, y = i, j
        for l in range(y-1, -1, -1):
            if matrix[x][l] != 0 and matrix[x][l] != "a":
                matrix[x][l] = "a"
        # Right
        x, y = i, j
        for r in range(y+1, len(matrix[0])):
            if matrix[x][r] != 0 and matrix[x][r] != "a":
                matrix[x][r] = "a"
        