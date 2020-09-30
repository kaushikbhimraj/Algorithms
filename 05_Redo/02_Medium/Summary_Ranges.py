

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
    	if not num:
    		return 

    	# Need two references, left and i. 
    	# i can be a pointer that is increments each iteration. 
    	# left holds a value at 0 initially and is incremented only when there is a mismatch. 
    	results = []
    	left = nums[0]
    	i = 1

    	while i < len(nums):
    		
    		if (nums[i] == nums[i-1]+1):
    			results.append(str(left) + "->" + str(nums[i])) if left != nums[i-1] else results.append(str(left))
    			left = nums[i]

    		i += 1

    	# Check and pdate results for last element. 
    	results.append(str(left) + "->" + str(right)) if left != nums[i-1] else results.append(str(left))
    	return results
