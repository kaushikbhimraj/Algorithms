"""
This question is about implementing a basic elimination algorithm for Candy Crush.

Given a 2D integer array board representing the grid of candy, different positive 
integers board[i][j] represent different types of candies. A value of board[i][j] = 0 
represents that the cell at position (i, j) is empty. The given board represents the state 
of the game following the player's move. Now, you need to restore the board to a stable 
state by crushing candies according to the following rules:

    If three or more candies of the same type are adjacent vertically or horizontally, "crush" 
    them all at the same time - these positions become empty.

    After crushing all candies simultaneously, if an empty space on the board has candies on 
    top of itself, then these candies will drop until they hit a candy or bottom at the same 
    time. (No new candies will drop outside the top boundary.)

    After the above steps, there may exist more candies that can be crushed. If so, you need 
    to repeat the above steps.

    If there does not exist more candies that can be crushed (ie. the board is stable), then 
    return the current board.

You need to perform the above rules until the board becomes stable, then return the current 
board.

"""
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        # Traverse the columns.
        for c in range(len(board[0])):
            for r in range(len(board) - 2):
                num1, num2, num3 = abs(board[r][c]), abs(board[r+1][c]), abs(board[r+2][c])
                if (num1 == num2 and num1 == num3 and num1 != 0):
                    board[r][c] = -num1
                    board[r+1][c] = -num2
                    board[r+2][c] = -num3
        
        for r in range(len(board)):
            for c in range(len(board[0]) - 2):
                num1, num2, num3 = abs(board[r][c]), abs(board[r][c+1]), abs(board[r][c+2])
                if (num1 == num2 and num1 == num3 and num1 != 0):
                    board[r][c] = -num1
                    board[r][c+1] = -num2
                    board[r][c+2] = -num3
        
        # Crush part needs to be finished
        