class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """

        # Create four counters. These counters are little different from basic counters. 
        self.row = [0] * n
        self.col = [0] * n
        self.diag = 0
        self.adiag = 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        # Identify if player 1 or 2 and based on the that you could have a +1 to -1
        toAdd = 1 if player == 1 else -1

        # For every (row, col) ordered set, add or subtract 1 at location based on player 1 or 2.
        self.row[row] += toAdd
        self.col[col] += toAdd

        # If ordered set was on the diagnal. 
        if row == col:
            self.diag += toAdd

        # If ordered set was on anti-diagnal. 
        if col == (len(self.col) - row - 1):
            self.adiag += toAdd

        # If any of these four counters reach n size, then you have a winner!
        if abs(self.row[row]) == self.n or abs(self.col[col]) == self.n or abs(self.diag) == self.n or abs(self.adiag) == self.n:
            return player
            
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)