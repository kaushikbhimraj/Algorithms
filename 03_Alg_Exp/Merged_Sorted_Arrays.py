"""
Write a function that takes in a non-empty sorted arrays of integers and returns a merged list 
of all of those arrays. 

The integers in the merged list should be in sorted order.


INPUT:
arrays = [
		  [1, 5, 9, 21],
		  [-1, 0],
		  [-124, 81, 121],
		  [3, 6, 12, 20, 150]
		 ]

OUTPUT:
[-124, -1, 0, 1, 3, 5, 6, 9, 12, 20, 21, 81, 121, 150]
"""


from heapq import heappush, heappop

def mergeSortedArrays(arrays):
	# Use an array for store the sorted values from the heap. 
	newHeap = []
	sorted_array = []

	# Enter values from all K sub-arrays in arrays. 
	for i in range(len(arrays)):
		heappush(newHeap, (arrays[i][0], i, 0))

	# While removing the top value, make sure to insert the next element in the sub array. 
	# Check if pointer for the sub-array does not exceed its lenght. 

	while newHeap:
		minValue, row, col = heappop(newHeap)
		col += 1
		if col == len(arrays[row]):
			sorted_array.append(minValue)
			continue
		else:
			heappush(newHeap, (arrays[row][col], row, col))
		sorted_array.append(minValue)

	return sorted_array

# Driver Code
x = [[1, 5, 9, 21], [-1, 0], [-124, 81, 121], [3, 6, 12, 20, 150]]
print(mergeSortedArrays(x))

