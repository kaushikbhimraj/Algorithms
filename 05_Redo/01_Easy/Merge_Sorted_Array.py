"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""

class Solution:
	
	# Do not return anything, modify nums1 in-place instead. 
	def merge(self, nums1, m, nums2, n):
		# Since we know that nums2 is always going to be shorter than num1. 
		idx1 = 0
		idx2 = 0
		idx1_2 = len(nums2)

		# You would have two pointers. 
		# Pointer 1: @ 0 in the first array. 
		# Pointer 2: Points to the first zero in the first array.

		# Pointer 3: @ 0 in the second array. 
		while idx1 < len(nums1):

			if nums1[idx1] == 0:
				nums1 = nums1[:idx1] + nums2[idx2:]
				return nums1

			if nums1[idx1] <= nums2[idx2]:
				idx1 += 1

			# When the element in the first array is higher than the element in the second array
			# Switch the higher element with the zero positioned at Pointer 2. 
			# Copy element from Pointer 3 to Pointer 1. 
			# Increment all three pointers. 
			else:
				nums1[idx1_2] = nums1[idx1]
				nums1[idx1]   = nums2[idx2]

				idx1   += 1
				idx1_2 += 1
			
				idx2 += 1
		return nums1


# Test Cases
a = [1,2,3,0,0,0]
b = [2,5,6]

c = [1,4,5,0,0,0]
d = [2,3,6]

x = Solution()
print(x.merge(a,3,b,3))
print(x.merge(c,3,d,3))