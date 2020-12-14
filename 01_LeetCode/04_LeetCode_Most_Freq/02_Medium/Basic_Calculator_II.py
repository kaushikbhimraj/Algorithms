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
        # Each number is separated by one in four mathematical operations. 
        # So until an opeation is found, keep concatenating the objects. 
        # When an operation is reached while traversal, 
        #     + => append the concatenated integer to stack and reset
        #     - => append the (-1) * concantenated integer to stack and reset
        #     * => pop top of stack and multiply with concatenated integer and put it back on stack
        #     / => pop top of stack and divide with concantenated integer and put it back on stack
        # After iteration, simply return sum of values in stack. 
        
        stack = []
        sign = "+"
        curr = 0
        
        for i in range(len(s)):
            if s[i].isdigit():
                curr = (curr * 10) + int(s[i])
            if s[i] in "+-*/" or i == len(s)-1:
                if sign == "+":
                    stack.append(curr)
                elif sign == "-":
                    stack.append(-curr)
                elif sign == "*":
                    stack.append(stack.pop() * curr)
                else:
                    stack.append(int(stack.pop() / curr))
                sign = s[i]
                curr = 0
        return sum(stack)