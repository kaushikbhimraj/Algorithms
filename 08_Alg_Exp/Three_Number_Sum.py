"""
Write a fucntion that takes in a non-empty array of distinct integers and an integer 
representing a target sum. The function should find all triplets in the array that 
sum up to the target sum and return a two-dimensional array of all these triplets. 
The numbers in each triplet should be ordered in ascending order, and the triplets
themselves should be ordered in asceding order with respect to the numbers they hold.

If no three numbers sum up to the target sum, the function should return an empty array.

INPUT
array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

OUTPUT
[[-8,2,6],[-8,3,5],[-6,1,5]]

Notes:
	- array is distinct
"""

class Solution:

	# Sort the array first so you can find the target sum 
	def threeNumberSum(self, array, targetSum):
		array.sort()
		target_sum = []
		
		for i in range(len(array)):

			left  = i + 1
			right = len(array) - 1

			while left < right:
				sums = array[i] + array[left] + array[right]

				if sums == targetSum:
					target_sum.append([array[i], array[left], array[right]])
					left  += 1
					right -= 1

				elif sums > targetSum:
					right -= 1

				else:
					left += 1
		return target_sum


a = [12, 3, 1, 2, -6, 5, -8, 6]
print(Solution().threeNumberSum(a, 0))