"""
Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed 
mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square 
that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' 
to '8') represents how many mines are adjacent to this revealed square, and finally 'X' 
represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares 
('M' or 'E'), return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed, then change it to revealed 
blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square ('E') with at least one adjacent mine is revealed, then change it to 
a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.

T: O(n); S: O(n) where n is number of sqaures on the board.
"""

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if (not board):
            return []
        i, j = click
        
        # Game over if click is a mine. 
        if (board[i][j] == "M"):
            board[i][j] = "X"
            return board
        
        # Recursion if any other is clicked. 
        self.dfs(board, i, j)
        return board
    
    def dfs(self, board, i, j):
        if (board[i][j] != "E"):
            return 
        
        directions = [(-1,-1),(1,1),(-1,1),(1,-1),(0,-1),(0,1),(1,0),(-1,0)]
        count = 0
        
        # Count of all mines around current square. 
        for row, col in directions:
            row = i + row
            col = j + col
            if (row >= 0 and row < len(board) and col >= 0 and col < len(board[0]) and board[row][col] == "M"):
                count += 1
        
        # This part is a crucial step. 
        # If there are no mines around a square, continue recursion to reveal more boxes. 
        # If there is a mine, update the root square with count and return back to root. 
        if count == 0:
            board[i][j] = "B"
        else:
            board[i][j] = str(count)
            return
        
        # Recursion condition
        for row, col in directions:
            row = i + row
            col = j + col
            if (row >= 0 and row < len(board) and col >= 0 and col < len(board[0])):
                self.dfs(board, row, col)
                
        