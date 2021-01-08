
# Binary Search:
# -------------------------------
# Best & Worst: 
# Search - O(log n)

class BinarySearch:
	def __init__(self, arr, x):
		self.arr = arr
		self.x = x

	def recursive(self, left, right):
		if left > right:
			return False
		mid = left + right
		if self.x == self.arr[mid]:
			return True
		elif self.x < self.arr[mid]:
			return self.recursive(left, mid-1)
		elif self.x > self.arr[mid]:
			return self.recursive(mid+1, right)

	def iterative(self):
		left = 0
		right = len(self.arr) - 1
		while left < right:
			mid = left + right
			if self.x == self.arr[mid]:
				return True
			elif self.x < self.arr[mid]:
				right = mid-1
			elif self.x > self.arr[mid]:
				left = mid+1
		return False


# Output 
a = [2, 23, 212, 345, 899, 1024, 2123, 2342, 221234, 4532124]
print(BinarySearch(a, 221234).recursive(0, len(a)-1))
print(BinarySearch(a, 221234).iterative())
