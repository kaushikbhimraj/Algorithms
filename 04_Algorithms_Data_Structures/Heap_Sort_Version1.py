# Min-Heap-Sort
# Simple heap sort.
# Still need to add the heapify logic to convert a array to a heap array.  

class heapq:
	def __init__(self):
		self.heap = []

	# Push the inserted value in the heap, and start the sort when there 
	# are two more values in the heap. Following is a min heap. 
	def heappush(self, value):
		self.heap.append(value)
		if len(self.heap) > 1:
			end = len(self.heap)-1
			while end > 0:
				parent = end//2
				if self.heap[end] < self.heap[parent]:
					self.swap(end, parent)
					end = parent
				else:
					break

	# Pop minimum and replace with the max from bottom. 
	# Reorder heap. 
	def heappop(self):
		end = len(self.heap)
		if end < 1:
			return 
		top_value = self.heap[0]
		self.heap[0] = self.heap.pop(end-1)
		
		n = 0
		while (2*(n))+2 < end:
			left  = (2*n) + 1
			right = (2*n) + 2

			if self.heap[n] > self.heap[left] and self.heap[n] > self.heap[right]:
				if self.heap[left] > self.heap[right]:
					self.swap(n, right)
					n = right
				else:
					self.swap(n, left)
					n = left
			else:
				if self.heap[n] > self.heap[right]:
					self.swap(n, right)
					n = right
				else:
					self.swap(n, left) 
					n = left

	# Helper function to swap elements in place. 
	def swap(self, i, j):
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


# Create heap. 
y = heapq()
y.heappush(9)
y.heappush(7)
y.heappush(10)
y.heappush(1)
y.heappush(2)
y.heappush(5)
y.heappush(28)

# Pop to get the least value. 
y.heappop()