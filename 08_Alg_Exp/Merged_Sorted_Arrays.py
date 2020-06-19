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

class KMerge:
	def __init__(self):
		self.heap   = []
		self.arrays = None

	def sortall(self, arrays):
		# Creating an empty array to populate sorted values from the array. 
		sorted_array = []
		self.arrays  = arrays

		# Insert the first k values into heap. 
		for i in range(len(self.arrays)):
			self.heappush((self.arrays[i][0], i, 0))

		# Before value is removed from heap you insert a new value.
		while self.heap:
			minVal, row, col = self.heap[0]
			if col+1 < len(self.arrays[row]):
				self.heappush((self.arrays[row][col+1], row, col+1))
			print(self.heap)
			self.heappop()

			sorted_array.append(minVal)

		return sorted_array

	def heappush(self, value):
		self.heap.append(value)
		if len(self.heap) > 1:
			end = len(self.heap) - 1
			
			while end > 0:
				parent = end//2
				if self.heap[parent][0] > self.heap[end][0]:
					self.swap(parent, end)
					end = parent
				else:
					break

	def heappop(self):
		self.heap.pop(0)
		if self.heap:
			self.heap[0] = self.heap.pop()
			n = 0

			while 2*n + 2 < len(self.heap):
				left  = 2*n + 1
				right = 2*n + 2

				if self.heap[n][0] > self.heap[left][0] and self.heap[n][0] > self.heap[right][0]:
					if self.heap[left][0] < self.heap[right][0]:
						self.swap(n, left)
						n = left
					else:
						self.swap(n, right)
						n = right
				else:
					if self.heap[n][0] > self.heap[left][0]:
						self.swap(n, left)
						n = left
					else:
						self.swap(n, right)
						n = right
			

	def swap(self, i, j):
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


arrays = [[1, 5, 9, 21],[-1, 0],[-124, 81, 121],[3, 6, 12, 20, 150]]
x = KMerge()
print(x.sortall(arrays))

