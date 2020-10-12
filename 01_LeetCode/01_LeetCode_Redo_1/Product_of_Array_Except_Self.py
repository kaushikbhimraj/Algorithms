"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""

class Solution:

	# Apparently this method is not applicable to what the question is asking. 
	# Cannot use division (line 50)
	def productExceptSelf(self, nums):
		total_product = 1
		isZero = False
		zeroCount = 0

		# Part of this problem has to do with catching edge-cases with zeros. 
		# If there is only zero in all the elements of the array. The product for it 
		# should be just like one. 
		# If there is more than one zero in the array. The entire product will be zero. 
		for i in range(len(nums)):
			if nums[i] == 0:
				isZero = True
				zeroCount += 1

			if nums[i] == 0 and zeroCount > 1:
				total_product = 0
				break
			elif nums[i] != 0:
				total_product = total_product * nums[i]


		# Replace each element by its quotient
		# The edge-cases are also handled here. 
		for i in range(len(nums)):
			if nums[i] == 0:
				nums[i] = total_product
			else:
				if isZero:
					nums[i] = 0
				else:
					nums[i] = int(total_product/nums[i])
		return nums

a = [1,2,3,4]
b = [0,1]
c = [1,1,1,1,1]
d = [-1,0]
e = [0,1,0]

x = Solution()
print(x.productExceptSelf(a))
print(x.productExceptSelf(b))
print(x.productExceptSelf(c))
print(x.productExceptSelf(d))
print(x.productExceptSelf(e))