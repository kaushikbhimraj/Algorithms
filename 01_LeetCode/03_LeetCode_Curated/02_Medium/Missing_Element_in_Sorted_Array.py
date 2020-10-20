"""
Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost 
number of the array.

 

Example 1:

Input: A = [4,7,9,10], K = 1
Output: 5
Explanation: 
The first missing number is 5.
Example 2:

Input: A = [4,7,9,10], K = 3
Output: 8
Explanation: 
The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 3:

Input: A = [1,2,4], K = 3
Output: 6
Explanation: 
The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
 

Note:

1 <= A.length <= 50000
1 <= A[i] <= 1e7
1 <= K <= 1e8
"""

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        # Return the number of missing elements in nums.
        missing = lambda x: nums[x] - nums[0] - x
        
        # If the missing number is greater than number of missing elements in nums. 
        # Then return the kth element by adding (k - # of missing elements) to last element of nums. 
        n = len(nums)-1
        if k > missing(n):
            return nums[-1] + k - missing(n)
        
        idx = 1
        while missing(idx) < k:
            idx += 1
        
        return nums[idx - 1] + k - missing(idx - 1)
            
