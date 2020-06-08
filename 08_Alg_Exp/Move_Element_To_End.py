"""
You're given an array of integers and an integer. Write a function that moves all instances of that
integer in the array to the end of the array and returns the array. 

The function should perform this in place(i.e, it should mutate the input array) and doesn't need
to maintain the order of the other integers. 

INPUT
array  = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

OUTPUT
[1, 3, 4, 2, 2, 2, 2, 2]
"""

class Solution:

	# When you remove an element from the array then 
	def moveElementToEnd(array, toMove):
		i = 0
		while i < len(array):
			if array[i] == toMove:
				array.append(array.pop(i))
				print(array[i])
			i += 1
		return array


a = [2, 1, 2, 2, 2, 3, 4, 2]
x = Solution
print(x.moveElementToEnd(a, 2))
