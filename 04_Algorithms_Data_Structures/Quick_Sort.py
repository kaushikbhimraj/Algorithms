"""
Date:  03.01.2020
Notes:
	Idea behind in quick sort is divide and conquer
	The technique can be primarly broken into two stages. 
		- Recursive stack (the termination function will have to left and right index are not ascending)
		- Partitioning (for every stack call the array will be partioned into lower and higher values based on pivot and after partion the pivot will be updated for the next call in the stack.)

	Recursion:
	Every call on the stack will have be have indices that point to smaller sections of the arrays 
	These sections are sorted using the partition method, wher values are switched around. 

	Array Paritioning
	First choose a pivot value. 
	Using two indices (a, b) to the array and compare if a > pivot and b < pivot. Switch places if true. 

	TIME COMPLEXITY:  Worst case N || Ideal case Nlog(N)
	SPACE COMPLEXITY: N

"""

# The following technique works but the space complexity of the algorithm is not great. 
# Every call on stack is creating two new arrays in memory.
class Sort:
    def QuickSort(self, array):
        if len(array) <= 1:
            return array

        pivot = array[0]
        Left = [x for x in array if x < pivot]
        Right = [x for x in array if x > pivot]

        return self.QuickSort(Left) + [pivot] + self.QuickSort(Right)

# Driver code for the above technique. 
arr = [12, 34, 56, 3, 23, 213, 5, 3, 123]
c = Sort()
print(c.QuickSort(arr))








#------------------------------------------------------------------------------------------------------------
# MORE EFFECTIVE / FOOL PROOF WAY OF QUICK SORT
# Swaps array elements in place without creating copies of the array on call stack.

def Quicksort(arr):
	if len(arr) <= 1:
		return arr
	pivot = arr[0]
	left  = [x for x in arr if x < pivot]
	right = [x for x in arr if x > pivot]
	return Quicksort(left) + [pivot] + Quicksort(right)

"""
The sort can be divided into three functions. 
The first function is the main function that the stack will start on. 
The second function will be used to split the array into smaller parts recursively.
The third function will be used to quick sort the smaller segment.
"""
class Quicksort_2:
	def quick(self, arr):
		if len(arr) <= 1:
			return arr
		self.quick_recursive(arr, 0, len(arr)-1)
		return arr

	def quick_recursive(self, arr, low, high):
		if low >= high:
			return
		pivot = self.partition(arr, low, high)
		self.quick_recursive(arr, low, pivot)
		self.quick_recursive(arr, pivot+1, high)

	# Sorting the smaller partitions. 
	def partition(self, arr, low, high):
		i = low + 1
		j = high
		pivot = arr[low]

		while i <= j:
			if arr[i] < pivot:
				i += 1
			elif arr[j] > pivot:
				j -= 1
			elif arr[i] > pivot and arr[j] < pivot:
				self.swap(arr, i, j)
		self.swap(arr, low, j)
		return j

	# Swap functions in the array.
	def swap(self, arr, i, j):
		temp = arr[i]
		arr[i] = arr[j]
		arr[j] = temp


# Driver code to initiate the algorithm object structure.
a = [9,2,3,1,13,50,20,4]
print("Sorted using Quicksort.")
print(a)
# print(Quicksort(a))
print(Quicksort_2().quick(a))