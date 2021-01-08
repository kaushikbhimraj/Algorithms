
"""
Write a function that takes in two non-empty arrays of integers, finds the pair of numbers 
(one from each array) whose absolute difference is closest to zero, and returns an array
containing these two numbers, with the number from the first array in the first position. 

You can assume that there will only be one pair of numbers with the smallest difference. 

INPUT
arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

OUTPUT
[28, 26]
"""

class Solution:
	def smallestDifference(self, arrayOne, arrayTwo):
		least_apart = [0,0]

		# Sort the two arrays
		arrayOne.sort()
		arrayTwo.sort()

		least_diff  = abs(arrayOne[0] - arrayTwo[0])
		i, j = 0, 0

		while i < len(arrayOne) and j < len(arrayTwo):

			diff = abs(arrayOne[i] - arrayTwo[j])

			if diff < least_diff:
				least_diff = diff
				least_apart[0] = arrayOne[i]
				least_apart[1] = arrayTwo[j]

			if arrayOne[i] == arrayTwo[j]:
				i += 1
				j += 1

			elif arrayOne[i] > arrayTwo[j]:
				j += 1

			else:
				i += 1

		return least_apart


a = [2, 8, 9, 10, 20]
b = [1, 2, 4, 37]

c = [-1, 5, 10, 20, 28, 3]
d = [26, 134, 135, 15, 17]

x = Solution()
print(x.smallestDifference(a, b))
print(x.smallestDifference(c, d))

