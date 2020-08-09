"""
Given an array of size n, find the majority element. The majority element is the element that appears
more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""
# Time: O(n) 
# Space: O(n)

class Solution:
    
    # Use values from array as keys. If keys repeat count up stored value by one. 
    # Return the maximum value stored by keeping track of the values. 
    def majorityElement(self, nums: List[int]) -> int:
        cache = {}
        maxValue = 0
        maxCount = 0
        
        for i in range(len(nums)):
            if nums[i] in cache:
                cache[nums[i]] += 1
            else:
                cache[nums[i]] = 1
            
            # If count of a certain value exceeds more than half, return that value as max.
            if cache[nums[i]] > len(nums)//2:
                return nums[i]
                
            