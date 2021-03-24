"""
Given an `m x n` binary `matrix` filled with `0`'s and `1`'s, *find the largest square containing only* `1`'s *and return its area*.

**Example 1:**
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

**Example 2:**
Input: matrix = [["0","1"],["1","0"]]
Output: 1

**Example 3:**
Input: matrix = [["0"]]
Output: 0

**Constraints:**

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 300`
- `matrix[i][j]` is `'0'` or `'1'`.
"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Create a new dp array the same size as matrix. 
        # Get the minimum value from other squares
        dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        maxlen = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                    maxlen = max(maxlen, dp[i][j])
        
        return maxlen * maxlen