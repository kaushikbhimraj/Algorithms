"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular 
automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live 
(represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors 
(horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current 
state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, 
return the next state.

# T: O(m * n) S: O(m * n) where m is number of rows and n is number of columns on board.
"""
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        for i in range(len(board)):
            for j in range(len(board[0])):
                # here 2 is dead to alive
                if (board[i][j] == 0 and self.helper(board, i, j) == 3):
                    board[i][j] = 2
                # here -1 is alive to dead
                if (board[i][j] == 1 and self.helper(board, i, j) not in [2, 3]):
                    board[i][j] = -1
        
        for i in range(len(board)):
            
            for j in range(len(board[0])):
                # when you find a 2 you bring back to life
                if (board[i][j] == 2):
                    board[i][j] = 1
                    
                # when you find a -1 you kill
                if (board[i][j] == -1):
                    board[i][j] = 0
    
    def helper(self, grid, i, j):
        count = 0
        row = len(grid)
        col = len(grid[0])
        coords = [(-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1),(0,-1),(0,1)]
        for x, y in coords:
            x += i
            y += j
            if (x >= 0 and x < row and y >= 0 and y < col):
                count += grid[x][y] % 2
        return count