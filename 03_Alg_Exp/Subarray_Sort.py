"""
Write a function that takes in an array of at least two integers and returns an array
of the starting and ending indices of the smallest subarray in the input array that needs
to be sorted in place in order for the entire input array to be sorted. 

If the input array is already sorted, the function should return [-1, -1]

INPUT
array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]

OUTPUT
[3, 9]
"""

def subarraySort(array):
	subarray = [0, 0]
	min_misfit = float("inf")
	max_misfit = float("-inf")

	# Iterate through the array to find mis-fits. 
	for i in range(len(array)):

		# Line 27 has three conditions: these conditions catch any misfits in the sorted array. 
		# Case 1: i == 0 and currValue > nextValue
		# Case 2: i == len(array) -1 and currValue < prevValue
		# Case 3: i is not 0 or len(array)-1 and currValue < prevValue or currValue > nextValue
		if \
		(i == 0 and array[i] > array[i+1]) or \
		(i == len(array)-1 and array[i] < array[i-1]) or \
		(i > 0 and i < len(array)-1 and (array[i-1] > array[i] or array[i+1] < array[i])):
			min_misfit = min(min_misfit, array[i])
			max_misfit = max(max_misfit, array[i])

	# If there were no misfits, then return a set output. 
	if min_misfit == float("inf"):
		return [-1,-1]
	
	# There are two while loops, 
	# one from LEFT
	# second from RIGHT
	left = 0
	while min_misfit >= array[left] and left < len(array)-1:
		left += 1
	subarray[0] = left

	right = len(array)-1
	while max_misfit <= array[right] and right > 0:
		right -= 1
	subarray[1] = right

	return subarray


# Test Cases
a = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
b = [2, 1]
c = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,2]
print(subarraySort(a))
print(subarraySort(b))
print(subarraySort(c))



