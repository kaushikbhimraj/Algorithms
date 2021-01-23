"""
Given an array of integers nums and an integer threshold, we will choose a positive 
integer divisor, divide all the array by it, and sum the division's result. Find the 
smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of the division is rounded to the nearest integer greater than or equal to 
that element. (For example: 7/3 = 3 and 10/2 = 5).

It is guaranteed that there will be an answer.

 

Example 1:

Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the sum will 
be 5 (1+1+1+2). 
Example 2:

Input: nums = [44,22,33,11,1], threshold = 5
Output: 44
Example 3:

Input: nums = [21212,10101,12121], threshold = 1000000
Output: 1
Example 4:

Input: nums = [2,3,5,7,11], threshold = 11
Output: 3
 

Constraints:

1 <= nums.length <= 5 * 104
1 <= nums[i] <= 106
nums.length <= threshold <= 106

T: O(n log n); S: O(1)
"""

# This solution uses a simple binary search approach. 
# Limits left and right are from 1 to max integer in nums. 
# We are trying to find the closest integer to threshold. 
# So our condition is sum of each math.ceil division with a division (mid) between left and right <= threshold
# After searching through, return the left. (maximum value before the condition fails to meet)
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        from math import ceil
        
        def condition(divisor) -> bool:
            return sum(ceil(x / divisor) for x in nums) <= threshold
        
        left, right = 1, max(nums)
        while ( left < right ):
            
            mid = left + (right - left)//2
            if ( condition(mid) ):
                right = mid
            else:
                left = mid + 1
            
        return left
    