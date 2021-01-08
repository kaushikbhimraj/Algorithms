"""
Write a function that takes in an array of integers and returns an array of length 2 representing 
the largest range of integers contained in that array. The first number in the output array 
should be the first number in the range, while the second number should be the last number in 
range. 

A range of numbers is defined as a set of numbers that come right after each other in the set of
real integers. For instance, the output array [2, 6] represents the range {2, 3, 4, 5, 6}, which
is a range of length 5. Note that numbers doesn't need to be sorted or adjacent in the input 
array in order to form a range. 

You can assume that there will only be one largest range. 

INPUT
array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]

OUTPUT
[0, 7]
"""

def largestRange(array):

	# Need a value to keep track of the size of the array. 
	# Need a 2 value to store the min and max of the continous range
	longest_length = 0
	longest_length_array = []

	# Need a cache to store all the values from the given array. 
	# The values from the array are the keys and dictionary will have a boolena for the value.
	# This will avoid repetitions in counting. 
	cache = {}
	for val in array:
		cache[val] = True

	# For every value in the main array, check and see if there exists a value -1 and +1 in the dictionary. 
	# And count the number of values and record the count. (while you are doing this also make sure to mark the value you visit
	# in the dictionary as False.)

	for val in array:
		if not cache[val]:
			continue

		cache[val] = False
		current_length = 1

		left = val - 1
		right = val + 1
		
		# Loop to check if the value left of the main value exist in dictionary.
		while left in cache:
			cache[left] = False
			left -= 1
			current_length += 1

		# Loop to check if the value right of the main value exist in dictionary. 
		while right in cache:
			cache[right] = False
			right += 1
			current_length += 1

		# Check and update every iteration if the range is greater than the longest range. 
		# Also the update the 2-value array if the condition is true. 
		if current_length > longest_length:
			longest_length = current_length
			longest_length_array = [left+1, right-1]

	return longest_length_array

a = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]

print(largestRange(a))