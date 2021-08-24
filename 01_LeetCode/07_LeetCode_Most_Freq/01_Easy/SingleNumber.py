"""
Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without 
using extra memory?

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

Constraints:
1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""

# T: O(n); S: O(1) where n is length of nums.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # using bit manipulation XOR
        # num XOR 0   => num
        # num XOR num => 0
        # So iterating through the entire array will give you the single number. 
        single = 0
        for num in nums:
            single ^= num
        return single