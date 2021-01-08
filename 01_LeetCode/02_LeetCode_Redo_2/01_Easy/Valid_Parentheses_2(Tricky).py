"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

class Solution:
	def isValid(self, s):

		cache = {"{":"}","[":"]","(":")"}
		stack = []

		# Use stacks to load the values in if the keys exists in dictionary. 
		for i in range(len(s)):
			if s[i] in cache.keys():
				stack.append(s[i])
			else:

				# Catch if the first element is not in values. (If so the sequence will always be wrong)
				if not stack or s[i] != cache[stack.pop()]:
					return False
		
		# This will check if the stack is empty. 
		# For the string sequence to be valid, the stack shold be completely empty.  
		return not stack


a "()[]{}"
x = Solution()
