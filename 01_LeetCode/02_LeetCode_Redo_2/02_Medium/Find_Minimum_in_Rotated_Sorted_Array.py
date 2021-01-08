"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # Edge case
        if len(nums) == 1:
            return nums[0]
        
        # Two pointers for the binary search.
        left = 0
        right = len(nums)-1
        
        # Check if the first and last values in array are increasing, 
        # if so, the first value is the pivot (no rotation in array)
        if nums[left] < nums[right]:
            return nums[left]
        
        # The logic here is to use a modified binary search to detect an anamoly
        # in the strictly increasing arrangement in the array. Traverse the array, 
        # using the left and right normally. But every iteration check whether the 
        # udpated mid is less than its previous value or its next value is less than 
        # the mid. When you catch this anamoly, you return the mid + 1 or mid - 1. 
        while left <= right:
            mid = left + (right - left)//2
            
            # Check for pivot value everytime the mid is updated,
            # mid + 1
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            # mid - 1
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            
            # Standard traversal of binary search here. 
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid-1