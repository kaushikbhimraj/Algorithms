# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

# Start from top-right of the matrix. 
# When you find 1 move left store position of 1.
# When you find 0 move down
# Return last position of 1.

# Time:  O(N + M) N is rows and M is cols
# Space: O(1)

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        last_one = -1
        row, col = binaryMatrix.dimensions()
        
        curr_r = 0
        curr_c = col - 1
        while curr_r < row and curr_c >= 0:
            if binaryMatrix.get(curr_r, curr_c):
                last_one = curr_c
                curr_c -= 1
            else:
                curr_r += 1
        
        return last_one