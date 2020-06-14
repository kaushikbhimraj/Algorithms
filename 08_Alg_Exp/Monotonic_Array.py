"""
Write a function that takes in an array of integers and returns a boolen representing 
whether the array is monotonic. An array is said to be monotonic if its elements, from 
left to right, are entirely non-increasing or entirely non-decreasing. 

INPUT
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

OUTPUT
true
"""

class Solution:
	def isMonotonic(self, array):
		if len(array) > 1:
			i = 1
			if array[0] > array[1]:
				while i < len(array):
					if array[i] <= array[i-1]:
						i += 1
					else:
						return False
			elif array[0] < array[1]:
				while i < len(array):
					if array[i] >= array[i-1]:
						i += 1
					else:
						return False
			return True
		return True


a = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
b = [-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -8, -9, -10, -11]

x = Solution()
# print(x.isMonotonic(a))
print(x.isMonotonic(b))


