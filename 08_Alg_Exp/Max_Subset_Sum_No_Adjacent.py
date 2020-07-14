"""
Write a function that takes in an array of positive integers and returns the MAXIMUM
sum of non-adjacent elements in the array. 

If a sum can't be generated, the function should return 0.

INPUT:
array = [75, 105, 120, 75, 90, 135]

OUTPUT:
330

O(n) time complexity
O(1) space complexity

HOW WOULD YOU SOLVE THIS WITH NEGATIVE NUMBERS IN IT?
"""

def maxSubsetSumNoAdjacent(array):
	if not array:
		return

	if len(array) == 1:
		return array

	array[1] = max(array[0], array[1])
	for i in range(2, len(array)):
		array[i] = max(array[i-1], array[i-2] + array[i])

	return array[-1]



array = [75, 105, 120, 75, 90, 135]
print(maxSubsetSumNoAdjacent(array))
