"""
A magic index in array A[1...n-1] is defined to be an index such that A[1] = i. 
Given a sorted array of distinct integers, write a method to find a magic index, 
if one exists, in array A.

FOLLOW UP
"""

class Solution:
	def bruteForce(self, array):
		for i in range(len(array)):
			if array[i] == i:
				return i
		return -1

	# Recursion for non-repeats in array
	def magicIndexNonRepeats(self, array):
		return self.nonRepeatHelper(array, 0, len(array)-1)

	def nonRepeatHelper(self, array, start, end):
		if end < start:
			return -1

		mid = (start + end)//2
		if array[mid] == mid:
			return mid

		if array[mid] < mid:
			return self.nonRepeatHelper(array, mid+1, end)

		if array[mid] > mid:
			return self.nonRepeatHelper(array, start, mid-1)


	# Recursion for repeating numbers in array. 
	def magicIndexRepeats(self, array):
		return self.repeatHelper(array, 0, len(array)-1)

	def repeatHelper(self, array, start, end):

		if end < start:
			return -1

		# Compute the mid pointer location
		midIdx = (start + end)//2
		if array[midIdx] == midIdx:
			return array[midIdx]

		leftIdx = min(midIdx-1, array[midIdx])
		left = self.repeatHelper(array, start, leftIdx)
		if left >= 0:
			return left

		rightIdx = max(midIdx+1, array[midIdx])
		right = self.repeatHelper(array, rightIdx, end)
		return right


array = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
x = Solution()

# Method 1
print(x.magicIndexNonRepeats(array))

# Method 2
print(x.magicIndexRepeats(array
