"""
Given an integer array nums sorted in ascending order, and an integer target.
Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., 
[0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You should search for target in nums and if you found return its index, otherwise return -1.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:
1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is guranteed to be rotated at some pivot.
-10^4 <= target <= 10^4
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Edge-case
        if not nums or len(nums) == 0:
            return -1
        
        
        # SEARCH - 1
        # Search and find the position of the pivot point. 
        # Declare two pointers on each ends of the array. 
        left = 0
        right = len(nums) - 1
        
        # The end result of this binary search will give us the pivot point. 
        while left < right:
            # Calculate the mid first. 
            mid = left + (right - left) // 2

            # In a sorted array, its odd to have the right value less than mid. 
            if nums[mid] > nums[right]:
                left = mid + 1
            # Similarly if the left value is greater than mid will update the right. 
            else:
                right = mid
         
        # SEARCH - 2
        start = left
        left = 0
        right = len(nums) - 1
        
        # Regular binary search shall be conducted. 
        # Before that we need to decide 
        if target >= nums[start] and target <= nums[right]:
            left = start
        else:
            right = start
        
        # Implement regular binary search. 
        
        while left <= right:
            mid = left + (right - left)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1