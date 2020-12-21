"""
Given a sorted array of integers nums and integer values a, b and c. Apply a 
quadratic function of the form f(x) = ax2 + bx + c to each element x in the 
array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example 1:

Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]
Example 2:

Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]

"""

from heapq import heappush, heappop
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def quadratic(val):
            return a*(val**2) + b*val + c
        
        heap = []
        for x in nums:
            heappush(heap, quadratic(x))
        result = []
        for i in range(len(heap)):
            result.append(heappop(heap))
        return result