"""
Given an array nums of n integers, are there elements a, b, c in nums such that 
a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Array should be sorted. 
        # Create a new array to store results. 
        nums.sort()
        results = []
        
        # Iterate through the array, 
        # Each iteration, run a sub loop to check sub-sum is equal and opposite to number @ i.
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            left = i + 1
            right = len(nums) - 1
            
            while left < right:    
                # Pointers on both sides to sum and check if sum is ==  
                value = nums[i] + nums[left] + nums[right]
                
                if value == 0:
                    results.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                
                    left += 1
                    right -= 1
                    
                elif value > 0:
                    right -= 1
                
                else:
                    left += 1
        return results