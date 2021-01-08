"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets 
is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets 
are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits 
are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Example 4:
Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
 
Constraints:
1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""

# T: O((max(number)^(number of integers in string)) * )
class Solution:
    def decodeString0(self, s: str) -> str:
        # Use stack to pull substring. 
        # When you hit ], start popping from stack and build a string until you hit [ on stack.
        # Then pop [ from stack and extract number. 
        # Create in_string by multiplying the substring with number. 
        # Put the string back on the stack. 
        
        # When you hit another ], you start popping values again. 
        # Until end of the string. 
        stack = []
        for i in range(len(s)):
            if s[i] == "]":
                
                in_string = ""
                while (stack and stack[-1] != "["):
                    in_string = stack.pop() + in_string
                
                stack.pop()
                num = ""
                while (stack and stack[-1].isdigit()):
                    num = stack.pop() + num
                in_string = in_string * int(num)
                
                # MOST IMPORTANT STEP IN LOGIC!!!
                for char in in_string:
                    stack.append(char)
            else:
                stack.append(s[i])
        
        # Put everthing back together and return
        return "".join(stack)