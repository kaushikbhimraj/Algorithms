
"""
Date: 03.05.2020
Heaps:
------
	- Array representation of Binary Tree
		Binary trees can be represented in an array. 
		if node is at the nth position, 
			1st child: 2*n
			2nd child: 2*n + 1
			parent from the child: (n)//2

			HEIGHT OF A COMPLETE BINARY TREE IS LOGN.
	
	- Complete Binary Tree

		Full binary tree: With respect of the height of the binary tree, when a tree has maximum number of nodes. 
						  Number of nodes for a tree of height n is (2^(n + 1) - 1)

		Complete binary tree: When the tree that is represented in array does not have gaps can be considered as 					   a complete tree. Or in other words, when the tree is a full binary tree till h-1 
							  where h is height of the binary tree and the last level is filled from left to right. 
	Heap
		Heap is always a complete binary tree. 
		Every node value is always greater/smaller than its children (2 child nodes). 
		Min and max heaps are arranged with the minimum and maximum values at the top of the tree. 

	- Insert 
		Considering a max heap for the insertion operation. 
		In order to insert a new value in a heap, it should be added as the last node in the tree (In other words, it will have to be added to the last element in the heap array). From the last element, this value will be compared with it parent node, if the value is greater, the values will be switched. This will continue as far as the root of the node if the value is greater than all its parent nodes. 
		TIME COMPLEXITY: Insertion can range from O(1) to O(LOG(N))

	- Delete
		Have to remove the root element first. (Can only remove either max or min depend on min/max type)
		When the top element is removed, it will have to be replaced by the last element in the complete binary tree will take its place. Here this trigger comparision with its children and will be replaced with the max of its children. This will keep going until otherwise or until the node will become a leaf node in the tree. 
		TIME COMPLEXITY: Deletion LOG(N)

	- Heap Sort
		For the heap sort, first the heap should be creating using N elements . 
		TIME COMPLEXITY: NLOG(N)
		If the top node (max/min) is deleted and added to an array the outcome will be a sorted array. 
		TIME COMPLEXITY: NLOG(N)

		TOTAL TIME: 2*N(LOG(N))

	- Heapify
		

	- Priority queues

"""
class Heap:

	# For heap sort the given unsorted array should be converted to a heap. This process can be termed as heapify. For the following algorithm a new array will have to be created and the values will have to copied over in a heap arragement. 
	def heapify(self, arr):
		if len(arr) <= 1:
			return arr
		heap = []
		for i in range(len(arr)):
			heap.append(arr.pop(0))
			i = len(heap) - 1
			while i >= 0:
				parent = i//2
				if heap[i] > heap[parent]:
					self.swap(heap, i, parent)
					i = parent
				else:
					i -= 1
		return heap

	# Heap sort will remove the top most value from the heap, append the value to a another array and re-organize heap. This will continue until all the values from the heap are appended to the second array. The issue is to deal with pop null array and out bound index values. 
	def heapsort(self, heap):
		output = []
		for i in range(len(heap)):

			# Making sure there are more than one value to pop
			if len(heap) <= 1:
				output = [heap.pop(0)] + output
				continue
			else:
				output = [heap.pop(0)] + output
				heap = [heap.pop(-1)] + heap
				n = 1

				while (2*n) < len(heap):
					node = n-1
					left = (2*n) - 1
					righ = (2*n)
					if heap[node] < heap[left] and heap[node] < heap[righ]:
						if heap[left] > heap[righ]:
							self.swap(heap, node, left)
							n = left
						else:
							self.swap(heap, node, righ)
							n = righ
					elif heap[left] < heap[node] < heap[righ]:
						self.swap(heap, node, righ)
						n = righ
					elif heap[righ] < heap[node] < heap[left]:
						self.swap(heap, node, left)
						n = left
					else:
						n += 1
		return output


	# This is a helper function that is used to swap array elements in place when creating a heap struction. 
	def swap(self, arr, i, j):
		arr[i], arr[j] = arr[j], arr[i]


# EXTRA METHODS
# --------------------------------------------------------------------------------------------------------

	# The output from the heapify algorithm will be used to create a sorting algorithm that will re-sort everytime an element is plucked from the root of the tree. 
	def reorganize(self, heap):
		output = heap.pop(0)
		heap = [heap.pop(-1)] + heap
		n = 1

		while (2*n) < len(heap):
			node = n-1
			left = (2*n) - 1
			righ = (2*n)
			if heap[node] < heap[left] and heap[node] < heap[righ]:
				if heap[left] > heap[righ]:
					self.swap(heap, node, left)
					n = left
				else:
					self.swap(heap, node, righ)
					n = righ
			elif heap[left] < heap[node] < heap[righ]:
				self.swap(heap, node, righ)
				n = righ
			elif heap[righ] < heap[node] < heap[left]:
				self.swap(heap, node, left)
				n = left
			else:
				n += 1
		return heap

	# To put the heap array into a more friendly format. 
	def traverse(self, heap):
		n = 1

		while (2*n) < len(heap):
			print("Parent: ", heap[n-1])
			print("ChildL: ", heap[(2*n) - 1])
			print("ChildR: ", heap[2*n])
			print("\n")
			n += 1
		if not len(heap)%2:
			print("Parent: ", heap[n-1])
			print("ChildL: ", heap[(2*n) - 1])








# DRIVER CODE
# --------------------------------------------------------------------------------------------------------
# a = [9, 2, 1, 4, 3, 5, 7, 6, 8, 10]
a = [9, 2, 1, 4, 3, 5, 7, 6, 8, 10, 110, 210, 97, 85]
print("This the un-sorted input array: ", a)

b = Heap().heapify(a)
print("Given array converted to heap:  ", b)

c = Heap().heapsort(b)
print("Array is sorted using heapsort: ", c)

# Heap().traverse(c)