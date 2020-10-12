"""
Given an array nums of n integers and an integer target, find three integers in nums such that 
the sum is closest to target. Return the sum of the three integers. You may assume that each 
input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 

Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Find the least distance. 
        dist = float("inf")
        
        # Use the same initial logic as 3 sum. 
        # Sort the array. 
        nums.sort()
        
        # Traverse through each element 
        for i in range(len(nums)):
            # Create left and right pointers. 
            l = i + 1
            r = len(nums) - 1
            
            # Traverse from both sides and calculate sum. 
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                
                # Update dist with min target - sum distance. 
                if abs(target-total) < abs(dist):
                    dist = target-total
                
                # Adjust pointers based on sum. 
                if total < target:
                    l += 1
                else:
                    r -= 1
            
            # If the distance is zero, you have found exact match. 
            if dist == 0:
                break
        
        # Return closest 3-sum. 
        return target - dist