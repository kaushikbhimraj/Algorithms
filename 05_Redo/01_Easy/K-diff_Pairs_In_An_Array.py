"""
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs 
in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers 
in the array and their absolute difference is k.

Example 1:

Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:

Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:

Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
Note:

The pairs (i, j) and (j, i) count as the same pair.
The length of the array won't exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].
"""

# Time: O(n**2)
# Space: O(1)

class Solution:
    # Brute force
    # Iterate through all combination and check it equals to k.
    def findPairs(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if (nums[i] - nums[j] == k):
                    count += 1
        return count

    def findPairs_Hashmap(self, nums: List[int], k: int) -> int:        
        # Store all counts of a value form nums in dictionary. 
        cache = collections.Counter(nums)
        count = 0
        
        # There are two distinctions in this problem
        # Check for k > 0 and k == 0, for the latter, check if count is greater than one for net to zero out
        for key in cache:
            if (k > 0 and key - k in cache):
                count += 1
            elif (k == 0 and cache[key] > 1):
                cache[key] -= 1
                count += 1
        return count