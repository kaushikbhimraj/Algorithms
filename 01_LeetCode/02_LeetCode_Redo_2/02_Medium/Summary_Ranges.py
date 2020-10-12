

"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
"""

# Array is sorted.
# Non-duplicate values in array. 
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        # Two pointers, slow and fast. 
        # Update the slow only when a break is found. 
        results = []
        start, i = 0, 0
        
        # Using a helper function to build string
        while i < len(nums)-1:
            if (nums[i] + 1 != nums[i + 1]):
                results.append(self.helper(nums[start], nums[i]))
                start = i + 1
            i += 1
        
        # Make sure to capture the last value. 
        results.append(self.helper(nums[start], nums[i]))
        return results
    
    def helper(self, one, two):
        if one == two:
            return str(one)
        else:
            return str(one) + "->" + str(two)
