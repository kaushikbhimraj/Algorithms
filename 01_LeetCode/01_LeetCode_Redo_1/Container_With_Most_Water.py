"""
Question: 11
Container With Most Water
Given n non-negative integers, a1, a2, ..., an, where each represents a point at coordinate (i, a). n vertical lines are drawn such that the two endpoints of line i is at (i, a,) and (i, 0). Find the two lines, which together with the x-axis forms a container, such that the container contains the most water. 
"""

class Container:
	def maxArea(self, height: List[int]) -> int:
		i, j = 0, len(height)-1
		MaxArea = 0

		while i < j:
			x = j-i
			if height[i] < height[j]:
				temp = x * (height[j]-(height[j]-height[i]))
				i += 1

			elif height[j] < height[i]:
				temp = x * (height[i]-(height[i]-height[j]))
				j -= 1

			else:
				temp = x * height[j]
				i += 1
				j -= 1

			if temp > MaxArea:
				MaxArea = temp

		return MaxArea


# Driver Code
a = [2,6,3,7,4,5,5,2]
print("Container with most water has an area of: " + str(Container().maxArea(a)))

