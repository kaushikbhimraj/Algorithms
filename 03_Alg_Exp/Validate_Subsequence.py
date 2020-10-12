"""
Given two non-empty arrays of integers, write a function that determines whether the second array is 
a subsequence of the first one. 

A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that
are in the same order as they appear in the array. For instance, the numbers [1,3,4] form a subsequence
of the array [1,2,3,4], and so do the numbers [2,4]. Note that a single number in an array and the array
iteself are both valid subsequence of the array. 

INPUT
array    = [5,1,22,25,6,-1,8,10]
sequence = [1,6,-1,10]

OUTPUT
True 

"""


class Solution:
	def isValidSubsequence(array, sequence):
		a_pointer = s_pointer = 0

		while a_pointer < len(array):
			if sequence[s_pointer] == array[a_pointer]:
				s_pointer += 1

			if s_pointer >= len(sequence) - 1:
				return True

			a_pointer += 1

		return False

			
