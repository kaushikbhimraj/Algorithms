"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements 
appear twice and others appear once.

Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""

class Solution:

	# Time: O(n)
	# Space: O(1)
	def findDuplicates(self, nums: List[int]) -> List[int]:
		# All the values in array can be considered indexes when nums[i]-1
		# When we visit the position, change value to negative. 
		# When value is already negative, add the positive to the new array. 
		results = []
		for i in range(len(nums)):
			index = abs(i)-1
			if nums[index] < 0:
				results.append(index+1)
			else:
				nums[index] = -nums[index]
		return results

	# Time: O(nlogn)
	# Space: O(1)	
    def findDuplicates2(self, nums: List[int]) -> List[int]:
        nums.sort()
        temp, i = 0, 0
        while i < len(nums):
            if temp != nums[i]:
                temp = nums.pop(i)
            else:
                i += 1
                
        return nums

