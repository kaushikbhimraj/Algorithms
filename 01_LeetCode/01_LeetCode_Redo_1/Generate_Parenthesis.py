"""

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""
class Solution:
	def generateParenthesis(self, n:int):
		outputArray = []
		self.backtracking(outputArray, "", 0, 0, n)
		return outputArray

	def backtracking(self, outputArray, string, openBrack, closeBrack, n):

		 # Base case
		 if len(string) == n*2:
		 	outputArray.append(string)
		 	return

		 # Make sure the there is always a open parenthesis before there is a closed. 
		 # Check whether the total number of open parenthesis is less than n.
		 # And make sure right parenthesis does not exceed the left parenthesis.
		 if openBrack < n:
		 	self.backtracking(outputArray, string+"(", openBrack+1, closeBrack, n)
		 if closeBrack < openBrack:
		 	self.backtracking(outputArray, string+")", openBrack, closeBrack+1, n)


# Test Code
a = 3

x = Solution()
print(x.generateParenthesis(a))