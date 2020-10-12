"""
Question: 46
Give a collection of distinct integers, return all possible permutations. 

Input:  [1,2,3]
Output: 
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Permutate:
	def __init__(self):
		self.perms = []

	def helper(self, i, array):
		if i == len(array)-1:
			print(i, array)
			self.perms.append(array[:])
		else:
			for j in range(i, len(array)):	
				self.swap(array, i, j)
				print(i, j, array)
				self.helper(i+1, array)
				self.swap(array, i, j)
		return self.perms

	def swap(self, array, i, j):
		array[i], array[j] = array[j], array[i]

x = [1,2,3,4]
Permutate().helper(0, x)
# print(Permutate().helper(0, x))