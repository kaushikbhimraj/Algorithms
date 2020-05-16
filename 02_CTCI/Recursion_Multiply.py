
import unittest

"""
RECURSION AND DYANMIC PROGRAMMING
Name: Recusion Multiply
Q No: 8.5
Desc: Write a recursive function to multiply two positive integers without using the 
	  * operator (or / operator). You can use addition, subtraction, and bit shifting, 
	  but you should minimize the number of those operations. 
"""


class withoutOperator:
	def bigSmall(self, x, y):
		if not isinstance(x, int) or not isinstance(y, int):
			raise TypeError("Inputs are not integer type.")

		if x < 0 or y < 0:
			raise ValueError("Numbers cannot be negative.")

		if x > y:
			return self.multiply(y, x)
		return self.multiply(x, y)

	def multiply(self, small, big):
		if small == 0:
			return 0

		# 1 * big = big
		if small == 1:
			return big

		half = self.multiply(small>>1, big)

		if small%2 == 0:
			return half + half
		return half + half + big


# Unit Tests
class TestwithoutOperator(unittest.TestCase):

	# Positive path test
	def test_bigSmall(self):
		self.assertEqual(withoutOperator().bigSmall(8, 9), 72)
		self.assertEqual(withoutOperator().bigSmall(9, 10), 90)
		self.assertEqual(withoutOperator().bigSmall(31, 35), 1085)

	# Check value
	def test_bigSmall_Negative(self):
		self.assertRaises(ValueError, withoutOperator().bigSmall, -9, 10)

	# Check the type
	def test_bigSmall_Type(self):
		self.assertRaises(TypeError, withoutOperator().bigSmall, "K", 3)


# Driver code
if __name__ == "__main__":
	unittest.main()