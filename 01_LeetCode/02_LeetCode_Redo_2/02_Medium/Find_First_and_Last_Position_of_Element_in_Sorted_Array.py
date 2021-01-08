
"""
Given an array of integers nums sorted in ascending order, find the starting and
ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

"""
# Time: O(logn + # of occurrences)
# Space: O(1)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Created two helper functions here. (To find the position of target element
        # and check its neighbors for repeats.)
        pos = self.binarSearch(nums, target)
        if pos != "None":
            return self.findNeighbors(nums, pos)
        else:
            return [-1, -1]
    
    
    # Check whether neighbors are repeats. Update left and right indexes. 
    def findNeighbors(self, nums, pos):
        left  = pos - 1
        right = pos + 1
        while left >= 0 and nums[left] == nums[pos]:
            left -= 1
        while right < len(nums) and nums[right] == nums[pos]:
            right += 1
        return [left+1, right-1]
    
    # Doing a simple binary search to find position of target element. 
    def binarSearch(self, nums, target):
        if len(nums) == 1 and nums[0] == target:
            return 0
        
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = left + right
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return "None"