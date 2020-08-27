"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent"
cells are those horizontally or vertically neighboring. The same letter cell may not be 
used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
 

Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # Iterate through board to the first alphabet of word 
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.findPath(board, word, i, j, 0):
                    return True
        return False
    
    # Helper method for backtracking 
    def findPath(self, board, word, i, j, idx):
        
        # If the pointer has reached end of string, sucess!
        if idx == len(word):
            return True
        
        # If i and j are out of bound or element in position does not match, fail!
        if i < 0 or i > len(board)-1 or j < 0 or j > len(board[0])-1 or board[i][j] != word[idx]:
            return False
        
        # Recursion
        # Before changing the variable store the previous state in temp. 
        temp = board[i][j]
        board[i][j] = " "
        found = self.findPath(board, word, i-1, j, idx+1) or\
        self.findPath(board, word, i+1, j, idx+1) or\
        self.findPath(board, word, i, j-1, idx+1) or\
        self.findPath(board, word, i, j+1, idx+1)
        
        # Restore the values to there location. 
        board[i][j] = temp
        
        return found