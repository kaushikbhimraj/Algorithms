"""
Given a string S, check if the letters can be rearranged so that two 
characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the 
empty string.

Example 1:

Input: S = "aab"
Output: "aba"

Example 2:
Input: S = "aaab"
Output: ""

Note:
S will consist of lowercase letters and have length in range [1, 500].
"""

class Solution:
	def reorganizeString(self, S: str) -> str:
		# Sort the string into any array based on character repetitions in it. 
		temp = sorted((S.count(x), x) for x in set(S))
		
		# Iterate through the sorted array and create a new array with only characters
		N = len(S)
		repeats = []
		for count, char in temp:

			# If the repetition count of a character in string is more than half the length
			# of string, it is impossible to arrange characters in string without consecutive 
			# repetitions.
			if (count > (N + 1)//2):
				return ""

			repeats.extend(char * count)

		# Arrange the characters in repeats
		res = [None] * N

		# Splice array and populate every alternate position with first half of repeats
		# Then splice array from second place (skipping alternate locations) and populate
		# every alternate position with second half of repeats
		res[::2], res[1::2] = res[N//2:], res[:N//2]

		return "".join(res)