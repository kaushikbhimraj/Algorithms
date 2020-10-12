"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the 
same color are adjacent, with the colors in the order red, white, and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Follow up:
Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?
 
Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
Example 3:

Input: nums = [0]
Output: [0]
Example 4:

Input: nums = [1]
Output: [1]

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2.
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # To play this game, you need three pointers
        # First two pointers start at 0
        # third pointer starts at the last element of array
        p1, p2, p3 = 0, 0, len(nums)-1
        
        # Rules of the game. 
        # If nums[p1] == 2, swap elements at p1 and p3, move p3 to left by 1. 
        # if nums[p1] == 0, swap elements at p1 and p2, move p1 and p2 to right by 1.
        # if nums[p1] == 1, move p1 to right by 1.
        # if p1 > p3, then the game is over.
        
        while p1 <= p3:
            if nums[p1] == 2:
                self.swap(nums, p1, p3)
                p3 -= 1
            
            elif nums[p1] == 0:
                self.swap(nums, p1, p2)
                p1 += 1
                p2 += 1
            
            else:
                p1 += 1
    
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]