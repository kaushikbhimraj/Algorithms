"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
        	return False

        y = x
        len_int = 0
        while y > 0:
        	len_int += 1
        	y //= 10

        if self._helper(x, len_int) == x:
        	return True
        return False

    def _helper(self, x, l):
    	total = 0
    	while x > 0:
    		total += (x%10) * (10**(l-1))
    		l -= 1
    		x //= 10
    	return total

x = 121
if Solution().isPalindrome(x):
	print("True")
else:
	print("False")