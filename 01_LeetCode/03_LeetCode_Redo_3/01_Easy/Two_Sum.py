"""
Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the 
same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

# Time: O(n); Space: O(n) where n is len(nums).
class Solution:
    def twoSum(self, nums, target):
        # Create a dictionary that would store the values in nums as keys and positions in nums
        # as values. 
        lookup = {}
        for pos, val in enumerate(nums):
            if target - val in lookup:
                return [pos, lookup[target-val]]
            else:
                lookup[val] = pos
        