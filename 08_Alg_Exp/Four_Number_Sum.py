"""
Write a function that takes in a non-empty array of distinct integers and an integer representing a 
target sum. The function should find all quadruplets in the array that sum up to the target sum and 
return a two-dimensional array of all these quadruplets in no particular order. 

If no four numbers sum up to the target sum, the function should return an empty array. 

INPUT
array = [7,6,4,-1,1,2]
targetSum = 16

OUTPUT
[[7,6,4,-1], [7,6,1,2]]
"""

def fourNumberSum(array, targetSum):

	all_sum_pairs = {}
	quadruplets   = []

	# Last element in the array can be skipped as it will be taken care in the nested loop.
	for i in range(len(array)-1):

		# Element after...
		# If difference of sum_1 of two numbers exists in the hash table, then append to OUTPUT 
		# There might be more sets of numbers that can sum to a key, so the key might have 
		# more than one set. (iterate through each set) line 33.
		for j in range(i+1, len(array)):

			sum_1 = array[i] + array[j]
			difference = targetSum - sum_1
			try:
				sum_pairs = all_sum_pairs[difference]
				for pair in sum_pairs:
					quadruplets.append(pair + [array[i], array[j]])
			except KeyError:
				pass

		# Elements before...
		# There elements that are before 'i' will be added to the hash table. 
		for k in range(0,i):

			sum_2 = array[k] + array[i]
			try:
				all_sum_pairs[sum_2].append([array[k], array[i]])
			except KeyError:
				all_sum_pairs[sum_2] = [[array[k], array[i]]]

	return quadruplets



a = [7,6,4,-1,1,2]
print(fourNumberSum(a, 16))


