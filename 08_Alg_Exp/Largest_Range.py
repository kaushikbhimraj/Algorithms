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
	cache = {}
	longest_subarray = []
	longest_range = 0

	longest_range_array = []

	# traverse array: twice
	# First: traverse to cache all elements in the dictionary
	for val in array:
		cache[val] = True

	# Second: traverse each element and check +1 and -1 of it exist in dictionary.
	# When a value is visited in the array mark it as visited in the dictionary. (avoid repeats)
	for i in range(len(array)):

		# Check value in cache is visited.
		if not cache[array[i]]:
			continue

		# else:
		cache[array[i]] = False
		current_range = 1
		left  = array[i] - 1
		right = array[i] + 1

		while left in cache:
			cache[left] = False
			current_range += 1
			left -= 1

		while right in cache:
			cache[right] = False
			current_range += 1
			right += 1

		if current_range > longest_range:
			longest_range = current_range
			longest_range_array = [left+1, right-1]

	return longest_range_array


a = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]

print(largestRange(a))