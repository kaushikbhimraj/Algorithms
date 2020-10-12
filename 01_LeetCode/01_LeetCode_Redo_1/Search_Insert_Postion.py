"""
Search Insert Position
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array. 

Example 1:
input:  [1, 3, 5, 6], 5
output: 2

Exmaple 2:
 input:  [1, 3, 5, 6], 2
 output: 1

Example 3:
input:  [1, 3, 5, 6], 7
output: 4

Example 4:
input:  [1, 3, 5, 6], 0
output: 0
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + right
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = right - 1
            
        return left

x = [1, 3, 5, 6]
target = 7
print(Solution().searchInsert(x, target))