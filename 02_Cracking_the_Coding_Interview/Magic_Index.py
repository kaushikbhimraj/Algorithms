

"""
RECURSION AND DYNAMIC PROGRAMMING
Question: 8.3
Name: 	  Magic Index
Desc: 	  A magic index in an array A[0...n-1] is defined to be an index such that A[i] = i. Given 
		  a sorted array of distinct integers, write a method to find a magic index, if one exists, 
		  in array A. 

Note: 	  WHAT IF THE VALUES ARE NON-DISTINCT?
"""
import unittest

class MagicIndex:

	def check(self, arr):
		self.checkHelper2(0, len(arr)-1, arr)
		return arr[0]

	# Values are returned only to the next call on the stack. So when a value is return in recursion, it 
	# is not able to make back out of the stack. To work around that, the first value of the arr is changed to a 
	# 0 or 1 based on the check. 

	# If a value is found to be equal to the index value, then the value at the index is returned. 
	# else a None is returned. 
	def checkHelper(self, low, high, arr):

		# Return condition
		if low > high:
			arr[0] = None
			return 

		mid = (high + low)//2

		if mid == arr[mid]:
			arr[0] = arr[mid]
			return

		elif mid > arr[mid]:
			self.checkHelper(mid+1, high, arr)
		else:
			self.checkHelper(low, mid-1, arr)

	
	# When the values in the array are distinct the above method will not work. 
	# The array will have to be split to left and right and computed in smaller sections.
	# IT STILL DOESN'T MAKE SENSE!!! 
	def checkHelper2(self, low, high, arr):

		if low > high:
			return

		arrIndex = (low + high)//2
		arrValue = arr[arrIndex]

		# This value is not able to flow up to the top.
		if arrIndex == arrValue:
			return arrValue

		leftValue = min(arrIndex-1, arrValue)
		left = self.checkHelper2(low, leftValue, arr)
		if left >= 0:
			print(left)

		rightValue = max(arrIndex+1, arrValue)
		right = self.checkHelper2(rightValue, high, arr)
		print(right)



# -------------------------------------------------------------------------------------------------
# Unit tests.
class TestMagicIndex(unittest.TestCase):

	def test_CheckHelper_Postive(self):
		self.assertEqual(MagicIndex().check([-23,-4,0,1,3,5,10]), 5)
		self.assertEqual(MagicIndex().check([-23,-4,0,1,3,5,10]), 5)
		self.assertEqual(MagicIndex().check([-23,-4,0,1,3,4,6]), 6)

	def test_CheckHelper_Negative(self):
		self.assertEqual(MagicIndex().check([-23,-4,0,1,3,4,10]), None)


if __name__ == '__main__':
	unittest.main()
