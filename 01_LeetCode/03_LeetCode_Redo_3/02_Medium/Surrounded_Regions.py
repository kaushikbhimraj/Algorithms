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
    # Only focus on 'O's along the border and move inwards.
    # When come across an 'O' change it to 'E'. 
    # After DFS, convert all left over 'O's to 'X' (these are still trapped :(
    # Change 'E' to 'O'
    # Viola!
    def solve_2(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(r,c):
            if (r < 0 or r >= m or c < 0 or c >= n):
                return
            
            if (board[r][c] != "O"):
                return
            
            board[r][c] = "E"
            
            for x,y in [(0,-1),(0,1),(1,0),(-1,0)]:
                dfs(r+x,c+y)
            
        m = len(board)
        n = len(board[0])
        for i in range(m):
            if board[i][0] == "O":
                dfs(i,0)
            if board[i][n-1] == "O":
                dfs(i,n-1)
            
        for j in range(n):
            if board[0][j] == "O":
                dfs(0,j)
            if board[m-1][j] == "O":
                dfs(m-1,j)
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j] == "O"):
                    board[i][j] = "X"
                elif (board[i][j] == "E"):
                    board[i][j] = "O"
            