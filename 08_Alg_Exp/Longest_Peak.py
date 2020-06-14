"""
Write a function that takes in an array of integers and returns the length of the longest peak in the array. 

A peak is defined as adjacent integers in the array that are strictly increasing until they reach a tip
(the highest value in the peak), at which point they become strictly decreasing. At least three integers are 
required to form a peak.

For example, the integers 1, 4, 10, 2 form a peak, but the integers 4, 0, 10 don't and niether do the integers
1, 2, 2, 0. Similarly the integers 1, 2, 3 don't form a peak because there aren't any strictly decreasing 
integers after the 3.

INPUT
array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

OUTPUT
6 (which is 0, 10, 6, 5, -1, -3)

Time:  O(n)
Space: O(1)
"""

class Solution:
	def longestPeak(self, array):
		longestPeak = 0
		i = 1

		# First try to find the peaks. 
		# The peaks cannot be the first or the last value in the array. 
		while i < len(array)-1:

			isPeak = array[i-1] < array[i] and array[i+1] < array[i]
			if not isPeak:
				i += 1
				continue

			# If you have a peak look at the left of it. 
			# Keep counting back until you either hit zero or a value that is greater than the previous. 
			leftIndex = i - 2
			while leftIndex >= 0 and array[leftIndex] < array[leftIndex + 1]:
				leftIndex -= 1

			# Do the same on the right of it and see the index doesnt exceed the length and values don't exceed the peaks. 
			# Right index can go up until the last element since it is not the peak. 
			rightIndex = i + 2
			while rightIndex < len(array) and array[rightIndex] < array[rightIndex - 1]:
				rightIndex += 1

			# Compute and update the peak length after iterating through each peak. 
			# VERY INTERESTING/SIMPLE WAY TO UPDATE THE MAX VALUE. (one liner)
			currentLongestPeak = rightIndex - leftIndex - 1
			longestPeak = max(longestPeak, currentLongestPeak)

			# Update the index with the right index value of from the peak. 
			i = rightIndex

		return longestPeak




# Test Case 
array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print(Solution().longestPeak(array))





