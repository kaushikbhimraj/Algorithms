"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
"""

class Solution:

	def trap(self, height) -> int:
		if not height or len(height) < 2:
			return 0

		# Index of tallest tower in array. 
		index = self.findMax(height)

		# Calculating area left of tower.
		pre_tallest_area = temp_height = 0
		i = 0
		
		while i <= index:
			
			if temp_height > height[i]:
				pre_tallest_area += temp_height - height[i]
			else:
				temp_height = height[i]
			i += 1

		# Calculating area right of tower.
		post_tallers_area = temp_height = 0
		j = len(height) - 1

		while j > index:

			if temp_height > height[j]:
				post_tallers_area += temp_height - height[j]
			else:
				temp_height = height[j]
			j -= 1

		return pre_tallest_area + post_tallers_area


	# Return index of tallest tower. 
	def findMax(self, height):
		tallest_tower = index = 0

		for i in range(len(height)):
			if tallest_tower < height[i]:
				tallest_tower = height[i]
				index = i

		return index

		

# Test Cases 
x = Solution()

a = [0,1,0,2,1,0,1,3,2,1,2,1]
print("\n")
print(a)
print("Area of rain water ", x.trap(a))

b = [0]
print("\n")
print(b)
print("Area of rain water ", x.trap(b))

c = [0,1]
print("\n")
print(c)
print("Area of rain water ", x.trap(c))

d = [0,1,0,3,0,0,0,0,0,0,0,0]
print("\n")
print(d)
print("Area of rain water ", x.trap(d))

e = [0,3,0,0,0,1]
print("\n")
print(e)
print("Area of rain water ", x.trap(e))
