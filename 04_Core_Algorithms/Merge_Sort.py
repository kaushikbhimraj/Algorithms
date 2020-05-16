
"""
Date: 02/29/2020
Notes:
	Major challenges regarding this algorithm is its mergesort recursion. 
	The recursion breaks the main array into single element arrays. 
	Each call in the stack will merge the elements in an ascending order and will result
	in an end output of a sorted array.

	The order can be changed to a descending order by simply inverting the conditions in the merge function. 

	TIME COMPLEXITY:	N * log(N) where N is the number of elements in the array
	SPACE COMPLEXITY:	N * log(N) 
"""
class Mergesort:

	# Main method the drives the merge sort recursively.
	def split_sort(self, arr):
		if len(arr) == 1:
			return arr
		mid = len(arr)//2
		leftHalfHalf  = arr[:mid]
		rightHalfHalf = arr[mid:]
		return self.merge(self.split_sort(leftHalfHalf), self.split_sort(rightHalfHalf))

	# Helper function used to merge two sorted arrys into one.
	def merge(self, leftHalf, rightHalf):
		output = [0]*(len(leftHalf) + len(rightHalf))
		i, j, k = 0, 0, 0

		while i < len(leftHalf) and j < len(rightHalf):
			if leftHalf[i] <= rightHalf[j]:
				output[k] = leftHalf[i]
				i += 1
			else:
				output[k] = rightHalf[j]
				j += 1
			k += 1
		while i < len(leftHalf):
			output[k] = leftHalf[i]
			i += 1
			k += 1

		while j < len(rightHalf):
			output[k] = rightHalf[j]
			j += 1
			k += 1

		return output








#------------------------------------------------------------------------------------------------------------
# This is a second way that optimizes the algorithm w.r.t space complexity. 
# The array is sorted in place. For this the array is copied only once and 
# then sorted using the copy as reference.

class MergeSort_2:
	def split_sort_2(self, arr):
		if len(arr) <= 1:
			return arr
		
		# Coying orginal array
		auxillaryArray = arr[:]
		self.mergeSortHelper(arr, 0, len(arr)-1, auxillaryArray)
		return arr

	def mergeSortHelper(self, arr, low, high, aux):
		if low == high:
			return 
		mid = (low + high)//2
		self.mergeSortHelper(aux, low, mid, arr)
		self.mergeSortHelper(aux, mid + 1, high, arr)
		self.merge_2(arr, low, mid, high, aux)

	def merge_2(self, arr, low, mid, high, aux):
		k = low
		i = low
		j = mid + 1
		while i <= mid and j <= high:
			if aux[i] <= aux[j]:
				arr[k] = aux[i]
				i += 1
			else:
				arr[k] = aux[j]
				j += 1
			k += 1

		while i <= mid:
			arr[k] = aux[i]
			k += 1
			i += 1

		while j <= high:
			arr[k] = aux[j]
			k += 1
			j += 1











# Driver code to initiate the algorithm object structure.
a = [9,2,3,1,13,50,20,4]

print("Sorting using the first method.")
print(a)
print(Mergesort().split_sort(a))

print("Sorting using the second method.")
print(MergeSort_2().split_sort_2(a))