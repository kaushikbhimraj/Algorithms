

"""
Implement next permutation, which rearranges numbers into the lexicographically next 
greater permutation of numbers. If such arrangement is not possible, it must rearrange 
it as the lowest possible order (i.e, sorted in ascending order). The replacement must 
be in-place and use only constant extra memory. Here are some examples. Inputs are in 
the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
	def nextPermutation(self, nums):

		# Starting from right end look for current value > previous value. 
		# When loop breaks, pointer points to value before the strictly decreasing section.
		i = len(nums)-2
		while i >= 0 and nums[i+1] <= nums[i]:
			i -= 1

		# Make sure the arrangment is not in last permutation. 
		if i >= 0:
			# Again loop from right end. 
			# Find immediate increament to value at i.
			j = len(nums)-1
			while j >= 0 and nums[j] <= nums[i]:
				j -= 1

			# Swap both values.
			self.swap(nums, i, j)

		# Reverse the strictly decreasing section of the permutation. 
		self.reverseArray(self, nums, i+1)


	# Helper to reverse array.
	def reverseArray(self, array, startIdx):
		endIdx = len(array)-1
		while startIdx < endIdx:
			self.swap(array, startIdx, endIdx)
			startIdx += 1
			endIdx -= 1

	# Helper to swap values in array.
	def swap(self, array, i, j):
		array[i], array[j] = array[j], array[i]
