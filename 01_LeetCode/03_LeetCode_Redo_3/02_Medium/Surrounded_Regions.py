"""
Given an m x n matrix board containing 'X' and 'O', capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.
 
Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on 
the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

Example 2:
Input: board = [["X"]]
Output: [["X"]]
 
Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def path(i, j):
            if (i < 0 or i > len(board)-1 or j < 0 or j > len(board[0])-1):
                return 1
            
            if ((i,j) in visited):
                return 0
            
            if (board[i][j] == "X"):
                return 0
            
            if ((i == 0 or i == len(board)-1 or j == 0 or j == len(board[0])-1) and board[i][j] == "O"):
                return 1
            
            around = [(-1,0),(1,0),(0,-1),(0,1)]
            neigh = 0
            for x, y in around:
                visited.add((i,j))
                neigh |= path(i+x, j+y)
                visited.remove((i,j))
                board[i][j] = "X" if not neigh else "O"
            return neigh
            
        neigh = 0
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j] == "O"):
                    path(i,j)