"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

# All methods,
# Time:  O(n*(2^n))
# Space: O(n*(2^n))

class Solution:
	def subsets(self, nums: List[int]) -> List[List[int]]:

		# Uses cascading to solve this problem. 
		output = [[]]
		for num in nums:

			# Each iteration you are taking a copy the entire output array
			# Looping through the copy and appending [num] to each element
			# Takeing the copy and concatenating it to the original output
			output += [curr + [num]  for curr in output]
		return output

	# This method uses backtracking to solve this problem
	def subsets2(self, nums: List[int] -> List[List[int]]:

		# Create a sub function to run the recursion inside. 
		# This is one of the easiest ways to run a recursion in python without worrying about I/Os. 
		def genSet(idx=0, curr=[]):
			
			# First thing, add a copy of curr to result array. 
			# Check if the set is complete before you add it. (It will be complete only when the size == nth count)
			if len(curr) == k:
				result.append(curr[:])

			# Then start itration through values from idx to n. 
			for i in range(idx, n):
				# Add the value @ nums[i] to current array before DFS.
				curr.append(nums[i])
				genSet(idx+1, curr)

				# Backtracking to add new elements to create more sets. 
				curr.pop()

		result = []
		n = len(nums)

		# Run loop to the nth iteration. 
		for k in range(n+1):
			genSet()

		return result