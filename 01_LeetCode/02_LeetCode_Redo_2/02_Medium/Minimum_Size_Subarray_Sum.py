"""
Given an array of n positive integers and a positive integer s, find the minimal 
length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 
0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the 
time complexity is O(n log n). 
"""

class Solution:
    
    # Sort of a SLIDING WINDOW problem.
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # If sum or value is greater than s, and length is less than current. Update it. 
        # If sum is >= s but the length is > current. Skip it. 
        
        # So this problem is asking for contigious array. 
        length = float("inf")
        left = 0
        right = 0
        
        # Computer running sum
        total = 0
        
        # When sum exceeds target, update length and decrement from left 
        # until sum is again less than target. 
        while right < len(nums):
            total += nums[right]
            
            while total >= s:
                length = min(length, right+1-left)
                total -= nums[left]
                left += 1
            
            right += 1
            
        # Check if length was not updated. 
        return length if length != float("inf") else 0