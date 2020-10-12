"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique 
combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

    	# Since this requires checking all combinations, we can use backtracking to implement it 
    	# relatively easily. First we need to declare an array to hold all the combinations. 
    	results = []

    	# Inorder to check if an element is repeated in candidates list and avoid unnecessary computation
    	# we sort the array. We need an index to keep track of position in array, another array to hold 
    	# the current combination. We also pass the results array to append all the combinations to it. 
    	self.helper(condidates.sort(), target, 0, [], results)

    	# after our magical recursive helper function populates the results array, we simply return it. 
    	return results


    def helper(self, candidates, target, idx, curr, results):

    	# Our base condition will check target is below zero. 
    	if target <= 0:

    		# Check also if it equal to zero. This tells us that we found a sum == target. 
    		# So append the combination in curr array to results. 
    		if target == 0:
    			results.append(curr)
    			return 

    		return 

    	# First we loop through each element in candidates starting from idx.  
    	for i in range(idx, len(candidates)):

    		# This condition is very important, it check whether i not in the starting position and 
    		# is equal to its previous value.
    		if i > idx and candidates[i] == candidates[i-1]:
    			continue

    		# Implementing a straight forward DFS where the target is decrement by the value at ith 
    		# position in cadidates array. The index idx is also incremented to push the recursion forward. 
    		self.helper(candidates, target - candidates[i], i + 1, curr + [candidates[i]], results)