

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice. 

Given 
	nums = [2, 7, 11, 15], target = 9

	return [0, 1]
	because nums[0] + nums[1] = 2 + 7 = 9


Notes: 	The solution was a lot more quicker and was able to write code a little more efficiently. 
"""

class Solution:
	def twoSum(self, nums, target):

		# {targer - nums[index]: index}
		dictionary = {}
		out = []
		for i in range(len(nums)):
			try:
				out.append(dictionary[nums[i]])
				out.append(i)
			except KeyError:
				dictionary[target-nums[i]] = i

		return out



# Test Cases
a = [2, 7, 11, 15]
b = [5, 5]
c = [3, 3]
d = [3, 2, 4]

# Targets 
a_t = 9
b_t = 10
c_t = 6
d_t = 6

x = Solution()
print(x.twoSum(a, a_t))
print(x.twoSum(b, b_t))
print(x.twoSum(c, c_t))
print(x.twoSum(d, d_t))