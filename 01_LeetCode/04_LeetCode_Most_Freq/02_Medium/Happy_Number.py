"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum 
of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:
Input: n = 2
Output: false

Constraints:
1 <= n <= 231 - 1
"""

class Solution:
	def isHappy(self, n: int) -> bool:

		# Create a nested function to get the sum of squares of digits in the int. 
		def happySum(number):
			digitSum = 0
			while number > 0:
				number, digit = number//10, number%10
				digitSum += (digit) ** 2
			return digitSum

		# Check if the sum is not 1 and 4. 
		# Because if we have a sum of 4, we know this will end in a loop. 
		# And if 1, it is a happy number. 
		while n != 1 and n != 4:
			n = happySum(n)

		# For every other scenario the operation will end in a result of 1.
		return n == 1