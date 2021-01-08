"""
Given an array of integers A, a move consists of choosing any A[i], 
and incrementing it by 1.
Return the least number of moves to make every value in A unique.

Example 1:

Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].
Example 2:

Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array
to have all unique values.

Note:
0 <= A.length <= 40000
0 <= A[i] < 40000
"""

class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        # Need to have a count
        # Sort the array.
        result = 0
        A.sort()
        
        # Start from position 1 and traverse to end. 
        for i in range(1, len(A)):
            # Check previous value >= current value 
            # If so, increment A[i] by A[i-1] + 1
            if (A[i-1] >= A[i]):
                result += A[i-1] - A[i] + 1
                A[i] = A[i-1] + 1
        
        # Return count
        return result