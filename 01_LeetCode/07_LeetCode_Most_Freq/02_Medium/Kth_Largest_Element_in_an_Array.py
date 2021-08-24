"""
Find the kth largest element in an unsorted array. Note that it is the kth 
largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

from heapq import _heapify_max, _heappop_max

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        _heapify_max(nums)
        
        # Now pop the nth value from the heap and return it. 
        for i in range(k):
            temp = _heappop_max(nums)
        return temp