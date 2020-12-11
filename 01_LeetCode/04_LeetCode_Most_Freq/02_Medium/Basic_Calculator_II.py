"""
Given a string S which represents an expression, evaluate this expression and return its
value. The integer division should truncate toward zero. 

Example 1:
Input: s = "3+2*2"
Output: 7

Example 2:
Input: s = " 3/2 "
Output: 1

Example 3:
Input: s = " 3+5 / 2 "
Output: 5
 
Constraints:
1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.

All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
"""

class Solution:
    def calculate(self, s: str) -> int:
        # Using a stack the mathematical operations can be performed. 
        stack = []
        sign = "+"
        curr = 0

        # Iterate through each character of string. 
        for i in range(len(s)):
        	# If the character can be converted to a digit, concatenate to the number. 
        	if s[i].isdigit():
        		curr = (curr * 10) + int(s[i])

        	# Skip spaces
        	# make sure you are not skipping the last character in the string. 
        	# also since first value in string will always be +ve and base 10. 
        	if s[i] in "+-*/" or i == len(s) - 1:
        		if sign == "+":
        			stack.append(curr)
        		elif sign == "-":
        			stack.append(-curr)
        		elif sign == "*":
        			stack.append(stack.pop() * curr)
        		else:
        			stack.append(int(stack.pop() / curr))

        		# reset the curr and update the sign. 
        		curr = 0
        		sign = s[i]
        return sum(stack)