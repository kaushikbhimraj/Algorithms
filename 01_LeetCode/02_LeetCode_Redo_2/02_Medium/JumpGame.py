"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which 
makes it impossible to reach the last index.

Constraints:

1 <= nums.length <= 3 * 10^4
0 <= nums[i][j] <= 10^5
"""

# Time: O(n)
# Space: O(1)

class Soluton:
	def canJump(self, nums: List[int]) -> bool:

		# Creat a variable to store the postion that you know is good index. 
		# Good index is an index that you can come back to from the previous index. 
		# If make sure you always start with a good index, you start with the last index of array. 
		lastGoodIndex = len(nums)-1

		# Iterate through all elements in array backwards
		# At each postion check if the index + nums[i] is greater than or equal to lastGoodPosition. 
		for i in reversed(range(len(nums)-1)):
			if i + nums[i] >= lastGoodPosition:
				lastGoodPosition = i

		# Only return true if position ends at 0. 
		# Else you know you were not able to jump back to a good position and were stuck there. 
		return lastGoodPosition == 0