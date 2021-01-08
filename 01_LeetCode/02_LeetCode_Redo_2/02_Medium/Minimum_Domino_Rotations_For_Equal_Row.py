"""
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the 
values in B are the same.

If it cannot be done, return -1.

Example 1:
Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 
2, as indicated by the second figure.

Example 2:
Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.

Note:
1 <= A[i], B[i] <= 6
2 <= A.length == B.length <= 20000
"""

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        
        # Since we are checking for the first elements,
        # handling this edge case is important. 
        if len(A) == 1:
            return 0
        
        a, b = A[0], B[0]
        val_A, val_B = True, True
        # Values @ position 0 in A and B need to be present in one or the other. 
        for i in range(1, len(A)):
            val_A = val_A and (True if A[i] == a or B[i] == a else False)
            val_B = val_B and (True if A[i] == b or B[i] == b else False)
        
        # One of two should always be true, if not return -1. 
        if not val_A and not val_B:
            return -1
        
        # Pick one or the other. 
        val = a if val_A else b
        
        # Count frequencies when val doesn't occur 
        # return min of both arrays. 
        countA, countB = 0, 0
        for i in range(len(A)):
            if A[i] != val:
                countA += 1
            if B[i] != val:
                countB += 1
            
        return min(countA, countB)

"""
E.g: 1
[2,1,2,4,2,2]
[5,2,6,2,3,2]

E.g: 2
[1,2,3,4,6]
[6,6,6,6,5]

E.g: 3
[1,4,1,6,6,1,6,2]
[2,2,5,3,1,5,6,6]

E.g: 4
[2,1,1,3,2,1,2,2,1]
[3,2,3,1,3,2,3,3,2]

E.g: 5
[1,2,1,1,1,2,2,2]
[2,1,2,2,2,2,2,2]
"""