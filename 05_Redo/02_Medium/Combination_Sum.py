"""
Given a set of candidate numbers (candidates) (without duplicates) and a target 
number (target), find all unique combinations in candidates where the candidate 
numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
 

Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
Each element of candidate is unique.
1 <= target <= 500
"""

# Time: O(2^n)
# Space: O(n)
# Where 'n' is number of candidates. 

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Create a results array to store all the possible sets that sum to target. 
        results = []

        # Using backtracking we can find all possible sets 
        self.findPaht(candidates, target, 0, [], results)
        return results


    def findPath(self, candidates, target, idx, tempArray, results):
    	# Base case 1
    	if (target == 0):
    		results.append(tempArray)
    		return

    	# Base case 2
    	if (target < 0):
    		return 

    	# Do a dfs using the for loop and see if target becomes zero. 
    	for i in range(len(candidates)):

    		# Avoid computation for repeats. 
    		if i == idx or candidates[i] != candidates[i-1]:
    			self.findPath(candidates, target - candidates[i], i, tempArray + [cadidates[i]], results)