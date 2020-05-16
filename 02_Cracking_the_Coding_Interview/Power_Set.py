
"""
RECURSION AND DYANMIC PROGRAMMING
Name: Power Set
Q No: 8.4
Desc: Write a method to return all subsets of a set.

Notes:
	  Apparently python sucks at copying arrays. 
	  It cannot copy objects that have lists, dicitonaries and objects in it. 
	  So will have use the python.copy.deepcopy

Time: O(2^n) where n is the number of elements in the input array. 

"""

from copy import deepcopy

class Subsets:
	def __init__(self):
		self.cache = [[]]

	def getAll(self, arr):
		self._helper(0, arr)
		self.printAll(self.cache)

	def _helper(self, arrIndex, array):

		if arrIndex > len(array)-1:
			return 

		# Copy the cache array into a separate copy for each call on stack
		CopiedCache = deepcopy(self.cache)
		arrValue    = array[arrIndex]

		# Iterate through the copied cache and append the value at the arrIndex to each element. 
		for i in range(len(CopiedCache)):
			CopiedCache[i].append(arrValue)

		# Append the New array to the original cache array. 
		self.cache += CopiedCache
		self._helper(arrIndex+1, array)

	def printAll(self, arr):
		for val in arr:
			print(val)


x = [3, 2, 12, 34, 21, 19, 43]
print(Subsets().getAll(x))