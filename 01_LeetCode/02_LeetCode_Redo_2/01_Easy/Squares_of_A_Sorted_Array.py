"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares 
of each number, also in sorted non-decreasing order.

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
"""

class Solution:
    
    def sortedSquares(self, A: List[int]) -> List[int]:
        
        # Traverse array, square each element and push values into heap, 
        # Pop values from heap to have values. 
        tempHeap = []
        for value in A:
            heapq.heappush(tempHeap, value**2)
        
        i = 0
        while tempHeap:
            A[i] = heapq.heappop(tempHeap)
            i += 1
        
        return A