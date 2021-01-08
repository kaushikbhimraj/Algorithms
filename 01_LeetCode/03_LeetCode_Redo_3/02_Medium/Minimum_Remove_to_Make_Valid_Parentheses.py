"""
Given a string of '(', ')' and lowercase English characters. 
Your task is to remove the minimum number of parenthesis ('(' or ')') in any positions )
so the resutling parenthesis string is valid if and only if:
	- It is the empty string, contains only lowercase characters, or
	- It can be written as AB (A concatenated with B), where A and B are valid strings, or
	- It can be written as (A), where A is a valid string. 

Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Example 4:
Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"

Constraints:
1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.
"""

class Solution:
	def minRemoveToMakeValid(self, s:str) -> str:
		# Create a stack to keep track ( brackets.
		# Store all the positions that need to be removed in a set.  
		stack = []
		toRemove = set()
		for i in range(len(s)):
			if s[i] == "(":
				stack.append(i)
			elif stack and s[i] == ")":
				stack.pop()
			elif not stack and s[i] == ")":
				toRemove.add(i)
			else:
				continue
		# MOST IMPORTANT POINT!!!
		# Have to combine the stack with toRemove set
		# The create a new string without the elements in toRemvoe set. 
		res = ""
		toRemove = toRemove.union(stack)
		for i,c in enumerate(s):
			if i not in toRemove:
				res += c
		return res