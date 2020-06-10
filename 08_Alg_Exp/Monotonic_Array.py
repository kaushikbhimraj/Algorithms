"""
Write a function that takes in an array of integers and returns a boolean representing whether the array is
monotonic. An array is said to be monotonic if its elements, from left to right, are entirely non-increasing
or entirely non-decreasing.

INPUT
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

OUTPUT
True

Time Comp:  O(n)
Space Comp: O(1)

"""

class Solution:
	def isMonotonic(self, array):
		is_decreasing = is_increasing = True

		# Elif condition is ignore the array[i] == array[i-1] values. 
		for i in range(1, len(array)):
			if array[i] > array[i-1]:
				is_decreasing = False
			elif array[i] < array[i-1]:
				is_increasing = False
		return is_decreasing or is_increasing



a = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
x = Solution()
print(x.isMonotonic(a))




