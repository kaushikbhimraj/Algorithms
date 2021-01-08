"""
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. 
If any two numbers in the input array sum up to the target sum, the fucntion should return them in an array, in
any order. If no two numbers sum up to the target sum , the function should return an empty array. 

Note that the target sum has to be obtained by summing two different integers in the array; you can't add a single
integer to iteself in order to obtain the target sum. 

You can assume that there will be at most one pair of numbers summing up the target sum. 

INPUT
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

OUTPUT
[-1 11]
"""

class Solution:
	def twoNumberSum(self, array, targetSum):
		if not array:
			return array
		cache = {}

		for i in range(len(array)):
			diff = targetSum - array[i]
			try:
				return [array[i], cache[array[i]]]
			except KeyError:
				cache[diff] = array[i]
		return []


array = [3, 5, -4, 8, 11, 1, -1, 6]
x = Solution()
print(x.twoNumberSum(array, 10))
