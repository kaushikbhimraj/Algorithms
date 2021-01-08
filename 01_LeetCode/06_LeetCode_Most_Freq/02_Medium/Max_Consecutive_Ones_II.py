"""
Given a binary array, find the maximum number of consecutive 1s in this array if you can 
flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
Follow up:
What if the input numbers come in one by one as an infinite stream? In other words, you 
can't store all numbers coming from the stream as it's too large to hold in memory. Could 
you solve it efficiently?
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev, curr, maxval = -1, 0, 0
        
        # There are two cases here, 
        # If values is 1 or 0:
        #   when 1: simply add to running sum./ 
        #   when 0: update prev sum and reset running sum. 
        # Every iteration, check and see if prev + 1 + curr is max. 
        # Here +1 is the zero being flipped and counted as 1. 
        
        for n in nums:
            if n == 1:
                curr += 1
            else:
                prev, curr = curr, 0
            
            maxval = max(maxval, prev + 1 + curr)
        return maxval