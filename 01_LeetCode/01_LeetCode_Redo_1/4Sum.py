"""
Given an array nums of n integers and an integer target, are there elements a, b, c and d
in nums such that a + b + c + d = target? Find all unique quadruplets in the array which
gives the sum of target.
"""

class Solution:
	"""
	This algorithm will be very similar to the two sum solution. 
	Will have a hash table to sum of two numbers and the values that compute the sum. 
	While iterating through each element, compute its sum with elements after it and
	check whether the difference exists in the hash map. If so return the pair from 
	the hash map and append the four values to the output array. 
	"""
	def fourSum(self, nums, target):
		cached_sum_pairs = {}
		four_sum_sets = []

		# To execute the above logic we need a parent loop to traverse the array. 
		for i in range(len(nums)-1):

			# Only looking at elements after the ith element in the array. 
			for j in range(i+1, len(nums)):

				forward_sum = nums[i] + nums[j]
				target_difference = target - forward_sum

				# Check target_difference exists in the hash table. 
				# The returned value might have more than one pairs that compute to difference. 
				try:
					sum_pairs = cached_sum_pairs[target_difference]
					for sum_pair in sum_pairs:
						four_sum_sets.append(sum_pair + [nums[i], nums[j]])

				except KeyError:
					pass

			# The second loop is used to add the sums of pairs before the ith element. 
			# This mitigates double counting. 
			for k in range(0, i):

				# Compute the sum of each element from the start of array with the ith element. 
				backward_sum = nums[k] + nums[i]

				try:
					cached_sum_pairs[backward_sum].append([nums[k], nums[i]])
				except KeyError:
					cached_sum_pairs[backward_sum] = [[nums[k], nums[i]]]

		return four_sum_sets


