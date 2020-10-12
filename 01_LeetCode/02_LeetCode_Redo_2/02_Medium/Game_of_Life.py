"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, 
is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). 
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the 
following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current
state. The next state is created by applying the above rules simultaneously to every cell in 
the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: 
You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, 
which would cause problems when the active area encroaches the border of the array. How would 
you address these problems?

"""

# NEED TO REMEMBER THE PREVIOUS STATE WHEN MAKING THE CHANGE
# Time: O(mn) where m is # of rows and n is # of columns. 
# Space: O(1)

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Traverse through board, when you find a value of 1
        # If there are more than three neighbors with '1' then make value 0
        # If there are two or three neighbors with '1' make value 1
        # If there are more than three neighbors with '1' make value 1. 
        # If value is '0' and three neightbors with '1' make value 0. 
        
        # Need to make a distinctions between current and previous state when you are changing values. 
        # For killing and bring back to life, we use two new states -1 -> dead and 2 -> bring back to life.
        # Live -> Dead (-1)
        # Dead -> Live (2)
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if board[i][j] == 0 and self.checkNeighbors(board, i, j) == 3:
                    board[i][j] = 2
                    
                elif board[i][j] == 1 and self.checkNeighbors(board, i, j) not in [2,3]:
                    board[i][j] = -1

        for i in range(len(board)):
        	for j in range(len(board[0])):
        		if board[i][j] == 2:
        			board[i][j] = 1
        		if board[i][j] == -1:
        			board[i][j] = 0
    
    # Helper function to check neighbors. 
    def checkNeighbors(self, board, row, col):
        count = 0
        
        # Above 
        if row-1 >= 0 and col-1 >= 0:
            count += board[row-1][col-1]%2
        if row-1 >= 0 and col+1 < len(board[0]):
            count += board[row-1][col+1]%2
        if row-1 >= 0:
            count += board[row-1][col]%2
        
        # Below
        if row+1 < len(board) and col-1 >= 0:
            count += board[row+1][col-1]%2
        if row+1 < len(board):
            count += board[row+1][col]%2
        if row+1 < len(board) and col+1 < len(board[0]):
            count += board[row+1][col+1]%2
        
        # Sides
        if col-1 >= 0:
            count += board[row][col-1]%2
        if col+1 < len(board[0]):
            count += board[row][col+1]%2

        return count