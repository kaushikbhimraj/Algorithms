"""
Count the number of prime numbers less than a non-negative number, n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0

Constraints:
0 <= n <= 5 * 106
"""

class Solution:
	def countPrime(self, n: int) -> int:
		# Create an array the will hold boolean for prime values. 
		# The logic here is to find multiples ahead using the current number. 
		# Iterate from 2 to n and count all the numbers that are prime. 
		notPrime = [False] * n
		count = 0
		for i in range(2, n):
			if not notPrime[i]:
				count += 1

				# Then make sure to populate all the values that multiples of this numbers with a True. 
				j = 2
				while (i * j < n):
					notPrime[i*j] = True
					j += 1
		return count