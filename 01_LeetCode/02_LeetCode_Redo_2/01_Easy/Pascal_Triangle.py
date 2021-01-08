"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

Time: O(row^2)
Space: O(row^2)
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Generate the triangle first
        triangle = [[1]*i for i in range(1, numRows+1)]
        
        for i in range(2, len(triangle)):
            for j in range(1, len(triangle[i])-1):
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
        
        return triangle