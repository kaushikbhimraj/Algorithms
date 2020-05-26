
"""
This program will contain solutions for both 3 and 2 sums. 

Name:     Two Sum
Level:    Easy
Question: Given an array of integers, return indices of the two numbers such 
		  that they add up to a specific target. You may assume that each input would have exactly one solution, 
		  and you may not use the same element twice. 

Name: 	  3Sum
Level: 	  Medium
Question: Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find 
		  all unique triplets in the array which gives the sum of zero. 

ISSUES:
	In line 73 the condition will count the value twice even if we only one element


THOUGHT PROCESS:
	first value:  					 for loop to iterate the array
	second value: 					 compliment of current value
	third value: 					 start with zero

	If second value is not found:	 second value -- && third value ++
	base case: 					 	 second value < 0 
	return array: 				 	 if there is a match for second and third values in array

"""

class sums:
	def __init__(self, arr):
		self.arr   = arr
		self.cache = None

	"""
	def twoSum(self, target):
		self.cache = {}
		
		for val in self.arr:
			self.cache[val] = val

		for i in range(len(self.arr)):
			diff = target - self.arr[i]
			try:
				return [target, self.arr[i], self.cache[diff]]
			except KeyError:
				pass
	"""


	def threeSum(self):
		# cache is used to store all zero sum sets. 
		# temp is used to add all the values that have already been used in the zero sets to avoid any repeats. 
		temp  	   = []
		self.cache = []

		for val in self.arr:

			if val not in temp:
				temp.append(val)
				results = self._helper((-1)*val,0, temp)
				if results:
					self.cache.append([val]+results)
			else:
				pass


	# recursive call used to check if second and third values are within the array.
	def _helper(self, second, third, repeatArr):
		if second == 0:
			return

		if second in self.arr and third in self.arr:
			repeatArr.append(second)
			repeatArr.append(third)
			return [second, third]

		dec = -1 if second > 0 else 1
		inc = 1 if second > 0 else -1

		return self._helper(second+dec, third+inc, repeatArr)



# Code Test
arr = [-1, 0, 1, 2, -1, -4]
x = sums(arr)
x.threeSum()
print("3 Sum:", x.cache)

