<<<<<<< HEAD
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


=======
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




>>>>>>> cc48bfaf32d1ecdb905b8407897287abfe78d263
