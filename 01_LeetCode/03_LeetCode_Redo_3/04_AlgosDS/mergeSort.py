"""
Implement Merge Sort:
	- Divide an array into two sub-arrays until you reach a single value in the array. 
	- Merge the values from there upwards. 
	- return the new array as the sorted array. 
"""

class Solution:

	def mergeSort(self, arr):
		if not arr:
			return arr
		return self.brkdwn(arr)

	def brkdwn(self, arr):
		if len(arr) == 1:
			return arr
		mid = len(arr)//2
		return self.merge(self.brkdwn(arr[:mid]), self.brkdwn(arr[mid:]))
	
	# T: O(n) and S:O(n) where n = max(len(a_1), len(a_2))
	def merge(self, a_1, a_2):
		i = 0
		j = 0
		res = []
		while i < len(a_1) and j < len(a_2):
			if a_1[i] <= a_2[j]:
				res.append(a_1[i])
				i += 1
			else:
				res.append(a_2[j])
				j += 1
		
		# Add the left overs to the end.
		end = a_1[i:] if i < len(a_1) else a_2[j:]
		return res + end

x = Solution()
a = [1,4,6]
b = [2,3,5]
print(x.merge(a, b))

c = [5,3,1,2]
print(x.mergeSort(c))